from abc import ABC, abstractmethod
import datetime
from decimal import Decimal
from enum import Enum


class TransactionType(Enum):
    """ Класс для определения типа транзакции (Доход/Расход) """
    INCOME = 0
    EXPENSE = 1


class Transaction:
    """
    Класс для создания транзакций с полями:
        дата, тип транзакции, количество и описание
    """

    def __init__(self,
            date: datetime.date,
            transaction_type: TransactionType,
            amount: Decimal, 
            description: str = None) -> None:
        self.date = date
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description


class BudgetPersistence(ABC):
    """ """
    @abstractmethod
    def read_transactions(self) -> list[Transaction]:
        pass

    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def update_transaction(self, index: int, transaction: Transaction) -> None:
        pass
