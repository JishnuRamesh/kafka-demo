from datetime import datetime
from .customer import Customer
from typing import Dict, Union


class Order:

    def __init__(self, customer: Customer, order_number: int, date_of_delivery: datetime, price: float, currency: str):
        self._customer = customer
        self._order_number = order_number
        self._date_of_delivery = date_of_delivery
        self._price = price
        self._currency = currency

    def as_dict(self) -> Dict[str, Union[str, float, int]]:
        """
        :return:  Returns Order object as dict
        """
        return {**self._customer.as_dict(),
                "order_number": self._order_number,
                "date_od_delivery": str(self._date_of_delivery),
                "price": self._price,
                "currency": self._currency
                }

    def get_order_number(self):
        """
        :return: Returns order number for the order
        """
        return self._order_number