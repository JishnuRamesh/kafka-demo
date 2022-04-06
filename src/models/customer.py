from uuid import uuid4
from typing import Dict


class Customer:

    def __init__(self, name: str, email: str, address: str, credit_card: str):
        self.customer_id = uuid4()
        self._customer_name = name
        self._customer_email = email
        self._customer_address = address
        self._customer_credit_card = credit_card

    def as_dict(self) -> Dict[str, str]:
        return {
            "customer_id": str(self.customer_id),
            "customer_name": self._customer_name,
            "customer_email": self._customer_email,
            "customer_address": self._customer_address,
            "customer_credit_card": self._customer_credit_card
        }
