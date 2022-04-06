from typing import Dict


class Config:

    def __init__(self):
        self._registry_url = "http://localhost:8081"
        self._kafka_url = "http://localhost:9092"
        self._topic_mapper = {"orders": "rawevents.orders.v1"}

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
