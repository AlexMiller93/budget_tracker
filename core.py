
import datetime


class Transaction:
    def __init__(self, balance, income, expenses, date, description):
    
        self.balance: int = balance
        self.income: int = income
        self.expenses: int = expenses
        self.date = date
        self.description: str  = description


class BudgetTracker:
    def __init__(self) -> None:
        self.transactions = None
        
    def add_income():
        pass
    
    def add_expense():
        pass