from src.kafka.schemaClient.schema_client import SchemaClient
from src.kafka.producer.kafka_producer import KafkaProducer
from src.orderApp.config import Config


class OrderAppProducer:
    _instance = None
    _config = Config()

    def __init__(self):
        raise NotImplementedError("Please call instance()")

    @classmethod
    def instance(cls):
        if not cls._instance:

            # Setup schema registry
            schema_client = SchemaClient(cls._config.get_schema_registry_config())

            # Create Kafka producer
            cls._instance = KafkaProducer(schema_client, cls._config.get_producer_kafka_conf())

        return cls._instance

    def produce_kafka_message(self, msg: dict, msg_key: str, topic: str):
        """
            Produces a message to the given Kafka topic
        :param msg: Message to send to Kafka topic
        :param msg_key: Key/identifier for message
        :param topic: Topic name to send message in
        """
        self.instance().produce(msg, msg_key, self._config.get_avro_schema_name(topic))
