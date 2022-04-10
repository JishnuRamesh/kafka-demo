from typing import Dict, List


class Config:

    def __init__(self):
        self._registry_url = "http://localhost:8081"
        self._kafka_url = "PLAINTEXT://localhost:9092"
        self._topic_mapper = {"orders": "rawevents.orders.v1"}
        self._consumer_group_id = "order_app_consumer_group"

    def get_schema_registry_config(self) -> Dict[str, str]:
        """
            Get configuration for schema registry
        :return: Dictionary of schema registry configuration
        """
        return {"url": self._registry_url}

    def get_producer_kafka_conf(self) -> Dict[str, str]:
        """
            Get configuration for Kafka Producer
        :return: Dictionary of Kafka configuration for producer
        """
        return {
            "bootstrap.servers": self._kafka_url,
        }

    def get_avro_schema_name(self, topic: str) -> str:
        """
            Gets the name of the avro
        :param topic: Name of the topic
        :return: Name of the avro schema
        """
        return self._topic_mapper[topic]

    def get_topics(self):
        """
            Return list of topics supported
        :return: List of topics
        """
        return self._topic_mapper.keys()

    def get_consumer_kafka_conf(self) -> Dict[str, str]:
        """
            Get configuration for Kafka Consumer
        :return: Dictionary of Kafka configuration for consumer
        """
        return {
            "bootstrap.servers": self._kafka_url,
            "group.id": self._consumer_group_id,
            "enable.auto.commit": "false",
            "auto.offset.reset": "earliest",
        }
