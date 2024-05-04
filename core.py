


class Transaction:
    def __init__(self, amount, date, description):
        self.amount: int = amount
        self.date = date
        self.description: str = description


class BudgetTracker:
    def __init__(self) -> None:
        # self.transactions = None
        self.balance: int = 0
        self.incomes: int = 0
        self.expenses: int = 0
        
    def add_income():
        pass
    
    def add_expense():
        pass