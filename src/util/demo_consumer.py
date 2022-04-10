from src.orderApp.OrderAppConsumer import OrderAppConsumer


def consume_messages():
    """
        Consumes messages from kafka
        based on topics subscribed by the consumer group
    """

    OrderAppConsumer().consume()
