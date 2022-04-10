from src.exceptions.kafka_exceptions import KafkaError


def kafka_consumer_exception_handler(ex: KafkaError):
    """
        Exception handler for Kafka exceptions
    :param ex: Exception from Kafka
    """
    # Handle exception as required by the application
    print(ex)

