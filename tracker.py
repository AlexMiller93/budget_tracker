from collections import namedtuple
import datetime
from decimal import Decimal
from core import BudgetStorage, Transaction, TransactionType

_Balance = namedtuple('Balance', ('income', 'expense'))


class BudgetTracker:
    """ Класс для хранения данных о транзакциях и балансе """

    def __init__(self, storage: BudgetStorage) -> None:
        self._storage = storage
        self._transactions: list[Transaction] = None
        self._balance: _Balance = None

    def get_total_income(self) -> Decimal:
        """ Метод для получения всех доходов """

        balance = self._get_balance()
        return balance.income

    def get_total_expenses(self) -> Decimal:
        """ Метод для получения всех расходов """
        balance = self._get_balance()
        return balance.expense

    def get_balance(self) -> Decimal:
        """ Метод для получения общего баланса """
        balance = self._get_balance()
        return balance.income - balance.expense

    def add_income(
        self,
        date: datetime.date,
        amount: Decimal,
        description: str = None
    ) -> None:
        """ Метод для увеличения дохода """

        self._add_transaction(
            date, TransactionType.INCOME, amount, description)

    def add_expense(self, date: datetime.date, amount: Decimal,
                    description: str = None) -> None:
        """ Метод для увеличения расхода """

        self._add_transaction(
            date, TransactionType.EXPENSE, amount, description)

    def update(
        self,
        index: int,
        date: datetime.date | None = None,
        amount: Decimal | None = None,
        description: str | None = None
    ) -> None:

        """ Метод для обновления данных (дата, сумма, описание)"""

        self._ensure_data()
        tran = self._transactions[index]
        if date is not None:
            tran.date = date
        if amount is not None:
            tran.amount = amount
        if description is not None:
            tran.description = description
        self.storage.update_transaction(index, tran)
        self._balance = None

    def search(
        self,
        is_income: bool | None = None,
        date: datetime.date | None = None,
        amount: Decimal | None = None
    ) -> list[tuple[int, Transaction]]:

        """ Метод для поиска данных (тип транзакции, дата, сумма)"""

        # определение типа транзакции в зависимости входных параметров
        if is_income is None:
            transaction_type = None
        elif is_income:
            transaction_type = TransactionType.INCOME
        else:
            transaction_type = TransactionType.EXPENSE
        self._ensure_data()

        # создание списка кортежей с искомыми транзакциями
        result = [(idx, tran) for (idx, tran) in enumerate(self._transactions) if
                (transaction_type is None or tran.type == transaction_type)
                and
                (date is None or tran.date == date)
                and
                (amount is None or tran.amount == amount)
                ]
        return result

    def clear(self) -> None:
        """ Метод для очистки данных о транзакциях, балансе, доходах и расходах """

        self._storage.delete_transactions()
        self._transactions = []
        self._balance = None

    def get_count(self) -> int:
        """ Метод для получения текущего количества транзакций"""

        self._ensure_data()
        return len(self._transactions)

    def _add_transaction(
        self,
        date: datetime.date,
        transaction_type: TransactionType,
        amount: Decimal,
        description: str = None
    ) -> None:
        self._ensure_data()

        # получение баланса
        balance = self._get_balance()
        tran = Transaction(
            date=date,
            transaction_type=transaction_type,
            amount=amount,
            description=description
        )
        self.storage.add_transaction(tran)
        self._transactions.append(tran)

        # подсчет баланса в зависимости от типа транзакции
        if transaction_type == TransactionType.INCOME:
            self._balance = _Balance(balance.income + amount, balance.expense)
        elif transaction_type == TransactionType.EXPENSE:
            self._balance = _Balance(balance.income, balance.expense + amount)

    def _get_balance(self) -> _Balance:
        if self._balance is None:
            self._ensure_data()
            income = Decimal(0)
            expense = Decimal(0)
            for tran in self._transactions:
                if tran.transaction_type == TransactionType.INCOME:
                    income += tran.amount
                elif tran.transaction_type == TransactionType.EXPENSE:
                    expense += tran.amount
            self._balance = _Balance(income, expense)
        return self._balance

    def _ensure_data(self) -> None:
        if self._transactions is None:
            data = self.storage.read_transactions()
            self._transactions = data

    def _clear_balance(self) -> _Balance:

        if self._balance is not None or self._transactions is not None:
            income = Decimal(0)
            expense = Decimal(0)
            self._transactions = []
            self._balance = _Balance(income, expense)
            return self._balance

        self.storage.clear_data()
