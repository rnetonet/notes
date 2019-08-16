"""Defines the Account class"""

from decimal import Decimal


class Account:
    """Mantain a bank account balance"""

    def __init__(self, name, balance):
        """Initialize the account"""

        # validate balance
        if balance < Decimal("0.00"):
            raise ValueError("balance must be > 0")

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit amount to the account"""

        if amount < Decimal("0.00"):
            raise ValueError("balance must be > 0")

        self.balance += amount

