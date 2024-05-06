from collections import namedtuple
import datetime
from decimal import Decimal
from core import BudgetPersistence, Transaction, TransactionType

_Balance = namedtuple('Balance', ('income', 'expense'))


class BudgetTracker:
    """ Класс для хранения данных о транзакциях и балансе """
    
    def __init__(self, persistence: BudgetPersistence) -> None:
        self._persistence = persistence
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
    
    def add_income(self, date: datetime.date, amount: Decimal,
                description: str = None) -> None:
        """ Метод для увеличения дохода """
        
        self._add_transaction(date, TransactionType.INCOME, amount, description)

    def add_expense(self, date: datetime.date, amount: Decimal,
                    description: str = None) -> None:
        """ Метод для увеличения расхода """
        
        self._add_transaction(date, TransactionType.EXPENSE, amount, description)
        
    def _add_transaction(self, date: datetime.date, type: TransactionType,
                        amount: Decimal, description: str = None) -> None:
        self._ensure_data()
        
        # получение баланса
        balance = self._get_balance()
        tran = Transaction(
            date=date,
            type=type,
            amount=amount,
            description=description
        )
        self._persistence.add_transaction(tran)
        self._transactions.append(tran)
        
        # подсчет баланса в зависимости от типа транзакции
        if type == TransactionType.INCOME:
            self._balance = _Balance(balance.income + amount, balance.expense)
        elif type == TransactionType.EXPENSE:
            self._balance = _Balance(balance.income, balance.expense + amount)
            
    def _get_balance(self) -> _Balance:
        if self._balance is None:
            self._ensure_data()
            income = Decimal(0)
            expense = Decimal(0)
            for tran in self._transactions:
                if tran.type == TransactionType.INCOME:
                    income += tran.amount
                elif tran.type == TransactionType.EXPENSE:
                    expense += tran.amount
            self._balance = _Balance(income, expense)
        return self._balance
    
    def _ensure_data(self) -> None:
        if self._transactions is None:
            data = self._persistence.read_transactions()
            self._transactions = data
