import json

from confluent_kafka.schema_registry import SchemaRegistryClient
from fastavro import parse_schema
from typing import Dict, Any, Tuple


class SchemaClient:

    def __init__(self, schema_conf: dict):
        self._client = SchemaRegistryClient(schema_conf)

    def get_schema_str(self, schema_id: int) -> str:
        """
            Gets schema string based on schema id
        :param schema_id: ID of the schema
        :return: Schema string
        """
        return self._client.get_schema(schema_id).schema_str

    def get_schema_dict(self, schema_id: int) -> Dict[Any]:
        """
            Get schema as a python dict
        :param schema_id: ID of the schema
        :return: Schema as a dict
        """
        return json.loads(self.get_schema_str(schema_id))

    def get_avro_schema(self, schema_id: int) -> str:
        """
            Returns a parsed avro schema
        :param schema_id:  ID of the schema
        :return: Returns a parsed avro schema
        """
        return parse_schema(self.get_schema_dict(schema_id))

    def get_latest_avro_schema_by_topic(self, topic: str) -> Tuple[int, dict]:
        """
            Gets schema id and avro schema
        :param topic: Name of the topic
        :return: Tuple of schema ID and parsed avro schema
        """
        subject = f"{topic}-value"
        latest_version = self._client.get_latest_version(subject).version
        schema_info = self._client.get_version(subject, latest_version)
        return schema_info.schema_id, parse_schema(
            json.loads(schema_info.schema.schema_str)
        )
