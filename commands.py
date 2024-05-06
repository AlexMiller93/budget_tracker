
from datetime import datetime
from decimal import Decimal
from core import Transaction, TransactionType
from data import FilePersistence
from tracker import BudgetTracker

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def add_transaction(tracker: BudgetTracker, persistence: FilePersistence) -> None:

    # выбираем тип транзакции
    category = input('''
Выберите тип транзакции доход или расход. Для этого нажмите (+/-) или (д/р): ''')
    
    # транзакции доход
    if category == '+' or category == 'д':
        value = input('Введите сумму: ')
        
        try:
            amount = Decimal(value=value, context=None)
        except ValueError:
            pass
        
        desc = input('Введите описание: ')
        
        if desc is None:
            desc = '-' * 5
            
        # создание даты и времени по формату
        date = datetime.now().strftime(DATE_FORMAT)    
        
        
        tracker.add_income(date=date, amount=amount, description=desc)
        print('Данные о доходе записаны!')
        
            
        transaction = Transaction(
            date=date,
            transaction_type=TransactionType.INCOME, 
            amount=amount, 
            description=desc)
        
        persistence.add_transaction(transaction)
        print('Данные о доходе записаны!')
        
        #?
        
    # транзакции расхода
    elif category == '-' or category == 'р':
        
        ...
        tracker.add_expense()
    
def edit_transaction(tracker: BudgetTracker) -> None:
    pass

def search(tracker: BudgetTracker) -> None:
    pass

def clear_data(tracker: BudgetTracker) -> None:
    pass