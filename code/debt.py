from dataclasses import dataclass
from typing import List, Optional

@dataclass
class User:
    user_number: str
    user_name: str
    bot_owner: bool

@dataclass
class Users:
    users = [User("Jan Kowalski", "+31123456789", True),
            User("Jan Nowak", "987654321", False),
            User("Anna Mickiewicz", "+48123432123", False),]

    def get_number_by_name(self, name: str) -> Optional[str]:
        for user in self.users:
            if user.user_name == name:
                return user.user_number
        return None

    def add_user(self, user: User) -> None:
        self.users.append(user)



@dataclass
class Transaction:
    user_number: str
    name: str
    amount: float
    currency: str = "EUR"


class Transactions:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def get_transactions_by_user(self, user_number: str) -> List[Transaction]:
        return [t for t in self.transactions if t.user_number == user_number]

    def get_all_transactions_with_no_user(self) -> List[Transaction]:
        return [t for t in self.transactions if t.user_number is None]

