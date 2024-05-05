class Transaction:
    def __init__(self):
        self.amount: int = 0
        self.date: str = None
        self.type: str = 'Income'
        self.description: str = None


class BudgetTracker:
    def __init__(self) -> None:
        self.transaction = Transaction()
        self.balance: int = 0
        self.incomes: int = 0
        self.expenses: int = 0
        
    def add_income():
        pass
    
    def add_expense():
        pass