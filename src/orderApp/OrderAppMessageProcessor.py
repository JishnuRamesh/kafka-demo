from exceptions.kafka_exceptions import KafkaError


def process_order(msg: dict):
    """
        Process the message received from consumer
    :param msg: Message as dict
    """

    print(f"Received message from kafka {msg}")


class OrderAppMessageProcessor:

    def __init__(self):
        self._processor_mapping = {"orders": process_order}

    def process_msg(self, msg, schema_name):

        # Call the correct processor function based on the schema name
        if schema_name in self._processor_mapping:
            self._processor_mapping[schema_name](msg)
        else:
            raise KafkaError(f"Message processor does not exist for {schema_name}")

