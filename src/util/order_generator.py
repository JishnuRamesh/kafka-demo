import random

from faker import Faker
from models.order import Order, Customer


class RandomOrderGenerator:

    def __init__(self, orders_required: int):
        self._orders_required = orders_required
        self._faker = Faker()

    def __iter__(self) -> Order:
        for _ in range(self._orders_required):
            customer = Customer(self._faker.name(), self._faker.email(),
                                self._faker.address())
            yield Order(customer,
                        random.randint(10000, 1000000),
                        self._faker.date_this_month(),
                        random.random(),
                        self._faker.currency_code())
