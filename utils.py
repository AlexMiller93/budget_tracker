import os

BUDGET_FILE = 'data/budget.txt'

""" 
Пример структуры данных в файле:
Дата: 2024-05-02
Категория: Расход
Сумма: 1500
Описание: Покупка продуктов

Дата: 2024-05-03
Категория: Доход
Сумма: 30000
Описание: Зарплата

"""

def create_file(filename: str):
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass

def write_data_in_file(filename: str, transaction: object): 
    with open(filename, 'a') as f:
        f.write(f"Дата: {transaction.date}\n")
        
        #? переменная для категории - доход\расход 
        f.write(f"Категория: {transaction.date}\n")
        
        # ? доход\расход 
        f.write(f"Сумма: {transaction.date}\n")
        
        f.write(f"Описание: {transaction.description}\n")

def save_transactions(transactions):
    # если файл есть, добавим запись
    if BUDGET_FILE.is_file():
        write_data_in_file(BUDGET_FILE)
            
    # если файла нет, создадим его и добавим запись
    else:
        create_file(BUDGET_FILE)
        write_data_in_file(BUDGET_FILE)
            
def load_transactions(transactions):
    with open(BUDGET_FILE, 'r') as file:
        pass
    
