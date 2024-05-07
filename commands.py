
import datetime
from tracker import BudgetTracker
from utils import handle_amount

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def add_transaction(tracker: BudgetTracker) -> None:

    # выбираем тип транзакции
    category = input('''
Выберите тип транзакции доход или расход. Для этого нажмите (+/-) или (д/р): ''')
    
    # транзакции доход
    if category == '+' or category == 'д':
        
        amount = handle_amount()
        desc = input('Введите описание: ')
                    
        # создание даты и времени по формату
        date = datetime.datetime.now().strftime(DATE_FORMAT)    
        
        tracker.add_income(date=date, amount=amount, description=desc)
        print('Данные о доходе записаны!')
        
    # транзакции расхода
    elif category == '-' or category == 'р':
        
        amount = handle_amount()
        desc = input('Введите описание: ')
        
        # создание даты и времени по формату
        date = datetime.datetime.now().strftime(DATE_FORMAT)    
        
        tracker.add_expense(date=date, amount=amount, description=desc)
        print('Данные о расходе записаны!')
    
def edit_transaction(tracker: BudgetTracker) -> None:
    
    print(""" 
Выберите какое поле вы хотите изменить: 

1. Сумма.
2. Описание
                """)
    choice = input("Выберите цифру (1/2/3): ")
    match choice:
                    
        # замена суммы
        case 1:
            amount = input('Введите искомое значение суммы: ')
            new_amount = input('Введите новое значение суммы: ')

            # логика замены
            
        # замена описания
        case 2:
            desc = input('Введите искомое описание: ')
            new_desc = input('Введите новое описание: ')
            
            if desc == new_desc:
                print('Вы пытаетесь изменить одни и те же слова в описании')
            
            # replace_word_in_file(BUDGET_FILE, desc, new_desc)
            
        
        case _:
            print('Некорректный выбор. Выберите цифру из предложенных вариантов (1/2/3)')

def search(tracker: BudgetTracker) -> None:
    target = input('Введите что вы хотите найти (тип транзакции, сумма, описание): ')
    
    # search_data()

def clear_data(tracker: BudgetTracker) -> None:
    choice = input('Вы точно хотите очистить данные с трекера? +/-: ')
    match choice:
        case '+':
            
            tracker.clear_balance()
            print('Данные с трекера удалены!')
        case '-':
            pass 
        case _:
            print('Некорректный выбор. Нажмите + или -')