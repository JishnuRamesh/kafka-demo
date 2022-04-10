from src.exceptions.kafka_exceptions import KafkaError


def process_order(msg: dict):
    """
        Process the message received from consumer
    :param msg: Message as dict
    """

    print(f"Received message from kafka {msg}")


class OrderAppMessageProcessor:

    def __init__(self):
        self._processor_mapping = {"orders": process_order}

    def process_msg(self, msg, topic_name):

        # Call the correct processor function based on the schema name
        if topic_name in self._processor_mapping:
            self._processor_mapping[topic_name](msg)
        else:
            raise KafkaError(f"Message processor does not exist for {topic_name}")

