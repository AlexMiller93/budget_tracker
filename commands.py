
import datetime
from decimal import Decimal
from core import Transaction, TransactionType
from data import FilePersistence
from tracker import BudgetTracker

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def add_transaction(tracker: BudgetTracker) -> None:

    # выбираем тип транзакции
    category = input('''
Выберите тип транзакции доход или расход. Для этого нажмите (+/-) или (д/р): ''')
    
    # транзакции доход
    if category == '+' or category == 'д':
        
        while True:
            value = input('Введите сумму: ')
            
            try:
                amount = Decimal(value=value, context=None)
                break
            except ValueError:
                pass
        
        desc = input('Введите описание: ')
        
        #! не работает
        if desc is None:
            desc = '-' * 5
            
        # создание даты и времени по формату
        date = datetime.datetime.now().strftime(DATE_FORMAT)    
        
        
        tracker.add_income(date=date, amount=amount, description=desc)
        print('Данные о доходе записаны!')
        
    # транзакции расхода
    elif category == '-' or category == 'р':
        
        while True:
            value = input('Введите сумму: ')
            
            try:
                amount = Decimal(value=value, context=None)
                break
            except ValueError:
                pass
        
        desc = input('Введите описание: ')
        
        # создание даты и времени по формату
        date = datetime.datetime.now().strftime(DATE_FORMAT)    
        
        
        tracker.add_expense(date=date, amount=amount, description=desc)
        print('Данные о расходе записаны!')
    
def edit_transaction(tracker: BudgetTracker) -> None:
    pass

def search(tracker: BudgetTracker) -> None:
    pass

def clear_data(tracker: BudgetTracker) -> None:
    choice = input('Вы точно хотите очистить данные с трекера? +/-:')
    match choice:
        case '+':
            tracker.clean_data()
        case '-':
            pass 
        case _:
            print('Некорректный выбор. Нажмите + или -')