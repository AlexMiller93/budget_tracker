
import datetime


class Budget:
    
    def __init__(self):
    
        self.balance: int = 0
        self.income: int = 0
        self.expenses: int = 0
        self.date = datetime.now()
        self.description: str | None = None

