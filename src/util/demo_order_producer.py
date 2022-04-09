from src.util.order_generator import RandomOrderGenerator
from src.orderApp.OrderAppProducer import OrderAppProducer


def produce_orders_to_kafka(number_of_orders: int):
    """
        Produces random orders to kafka using
        Order APP producer. Random orders are generated using
        order generator

    :param number_of_orders:  Number of orders to be sent
    """

    random_orders = RandomOrderGenerator(number_of_orders)
    #producer = OrderAppProducer()

    for order in random_orders:
        print(order.as_dict())
        #producer.produce_kafka_message(order.as_dict(), str(order.get_order_number()), "orders")

