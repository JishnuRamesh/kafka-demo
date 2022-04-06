import io
from struct import unpack

from confluent_kafka import Consumer
from fastavro import schemaless_reader
from kafka.schemaClient.schema_client import SchemaClient

from exceptions.kafka_exceptions import (
    KafkaDeserializationError,
    KafkaError,
    KafkaMessageError,
    KafkaMsgProcessorError,
)

from typing import List, Dict, Callable, Tuple


class KafkaConsumer:
    def __init__(
        self,
        schema_client: SchemaClient,
        topics: List[str],
        consumer_conf: Dict[str],
        exception_handler: Callable,
        msg_processor: Callable,
    ):
        self._schema_client = schema_client
        self._topics = topics
        self._msg_processor = msg_processor
        self._consumer = Consumer(consumer_conf)
        self._exception_handler = exception_handler

    def _get_schema_from_avro_message(self, msg) -> Tuple[dict, int]:
        """
            Gets parsed schema from avro message
        :param msg: Avro message from Kafka
        :return: Schema in json format
        """
        magic, schema_id = unpack(">bI", msg.read(5))

        if magic != 0:
            raise KafkaError(
                "Not a valid Kafka message, does not begin with the magic byte"
            )

        return (
            self._schema_client.get_avro_schema(schema_id),
            schema_id,
        )

    def _deserialize_avro_message(self, msg) -> Tuple[dict, int, str]:
        """
             Deserializes avro message from schema id given in the first 5 bytes
        :param msg: Avro message from Kafka
        :return: A tuple of decoded message, schema id and schema name
        """
        msg_value = msg.value()

        # Read message as bytes
        bytes_reader = io.BytesIO(msg_value)
        bytes_reader.seek(0)

        # Get schema from the bytes message
        schema, schema_id = self._get_schema_from_avro_message(bytes_reader)
        schema_name = schema["name"].split(".")[-1]

        # Read the bytes message using the schema
        return (
            schemaless_reader(bytes_reader, schema, reader_schema=schema),
            schema_id,
            schema_name,
        )

    def consume(self):
        """
            Continually polls Kafka topics and processes messages from it
        """
        try:
            # Subscribe to the topics
            self._consumer.subscribe(self._topics)

            while True:
                # Consume messages and call callbacks
                msg = self._consumer.poll(1)

                # Handle errors
                if msg is None:
                    continue
                if msg.error():
                    self._exception_handler(KafkaMessageError(msg.error()))
                    continue

                topic_name = msg.topic()

                try:
                    # Deserialize message
                    (
                        deserialized_message,
                        schema_id,
                        schema_name,
                    ) = self._deserialize_avro_message(msg)
                except Exception as ex:
                    self._exception_handler(
                        KafkaDeserializationError(
                            error_msg=str(ex), raw_message=msg.value(), topic=topic_name
                        )
                    )
                    self._consumer.commit(asynchronous=False)
                    continue

                try:
                    # Give deserialized message to message processor
                    self._msg_processor.process_msg(
                        deserialized_message, topic_name, schema_id, schema_name
                    )
                except Exception as ex:
                    self._exception_handler(
                        KafkaMsgProcessorError(
                            error_msg=str(ex),
                            deserialized_msg=deserialized_message,
                            topic=topic_name,
                            schema_id=schema_id,
                            schema_name=schema_name,
                        )
                    )

                # Signal successfully read message
                self._consumer.commit(asynchronous=False)
        finally:
            # Cleanly close consumer at the end
            self._consumer.close()