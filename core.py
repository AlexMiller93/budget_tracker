import abc
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
    
    def __init__(self, date: datetime.date, type: TransactionType,
                amount: Decimal, description: str = None) -> None:
        self.date: date
        self.type: type
        self.amount = amount
        self.description = description


class BudgetPersistence(abc.ABC):
    """ """
    @abc.abstractmethod
    def read_transactions(self) -> list[Transaction]:
        pass

    @abc.abstractmethod
    def add_transaction(self, transaction: Transaction) -> None:
        pass

    @abc.abstractmethod
    def update_transaction(self, index: int, transaction: Transaction) -> None:
        pass