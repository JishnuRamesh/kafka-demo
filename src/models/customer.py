from uuid import uuid4
from typing import Dict


class Customer:

    def __init__(self, name: str, email: str, address: str, credit_card: str):
        self._id = uuid4()
        self._name = name
        self._email = email
        self._address = address
        self._credit_card = credit_card

    def as_dict(self) -> Dict[str, str]:
        return {
            "id": str(self._id),
            "name": self._name,
            "email": self._email,
            "address": self._address,
            "credit_card": self._credit_card
        }
