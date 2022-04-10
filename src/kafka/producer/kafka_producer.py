import io

from confluent_kafka import Producer
from fastavro import schemaless_writer
from src.kafka.schemaClient.schema_client import SchemaClient

from src.exceptions.kafka_exceptions import KafkaEncodeMsgError, KafkaProduceError


class KafkaProducer:
    def __init__(self, schema_client:SchemaClient, producer_conf: dict):
        self._schema_client = schema_client
        self._producer = Producer(producer_conf)

    def _encode_message(self, msg: dict, topic: str) -> bytes:
        """
            Encodes a given message using the latest schema for the given topic
        :param msg: Message to be encoded
        :param topic: Topic name to send message in
        :return: Avro encoded version of msg
        """
        try:
            schema_id, schema = self._schema_client.get_latest_avro_schema_by_topic(topic)

            output = io.BytesIO()

            # Write the magic byte for the first byte
            output.write(int(0).to_bytes(1, byteorder="big"))

            # Write the schema id in the next four bytes
            output.write(schema_id.to_bytes(4, byteorder="big"))
            schemaless_writer(output, schema, msg)

            return output.getvalue()

        except Exception as ex:
            raise KafkaEncodeMsgError(error_msg=str(ex), raw_msg=msg, topic=topic)

    def produce(self, msg: dict, msg_key: str, topic: str):
        """
            Produces a given message to the given Kafka topic
        :param msg: Message to send to Kafka topic
        :param msg_key: Key/identifier for message
        :param topic: Topic name to send message in
        """
        # Serialize message
        coded_message = self._encode_message(msg, topic)

        # Produce the message
        try:
            self._producer.produce(topic=topic, key=str(msg_key), value=coded_message)
            self._producer.flush()
        except Exception as ex:
            raise KafkaProduceError(
                error_msg=str(ex),
                raw_msg=msg,
                msg_key=msg_key,
                encoded_msg=coded_message,
                topic=topic,
            )