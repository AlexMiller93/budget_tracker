
import datetime


class Budget:
    
    def __init__(self, balance, description):
    
        self.balance = balance
        self.date = datetime.now()
        self.description = description

