from src.kafka.schemaClient.schema_client import SchemaClient
from src.kafka.consumer.kafka_cosumer import KafkaConsumer
from src.orderApp.config import Config
from src.orderApp.exception_handler import kafka_consumer_exception_handler
from src.orderApp.OrderAppMessageProcessor import OrderAppMessageProcessor


class OrderAppConsumer:
    _instance = None
    _config = Config()

    @classmethod
    def instance(cls):
        if not cls._instance:

            # Setup schema registry
            schema_client = SchemaClient(cls._config.get_schema_registry_config())

            cls._instance = KafkaConsumer(
                schema_client,
                cls._config.get_topics(),
                cls._config.get_consumer_kafka_conf(),
                kafka_consumer_exception_handler,
                OrderAppMessageProcessor(),
            )

        return cls._instance

    def consume(self):
        """
            Consumes message from subscribed topics
        """
        self.instance().consume()
