import os


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

def handle_int_input():
    value = input('Введите значение: ')
    while True:
        try:
            value = int(value)
            break
        
        except ValueError:
            continue
            
    return value

def create_file(filename: str):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8'):
            pass
        
def write_data_in_file(filename: str, transaction: object): 
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"Дата: {transaction.date}\n")
        
        if transaction.type == 'Income':
            f.write(f"Категория: Доход\n")
            print('Доход записан')
        else:
            f.write(f"Категория: Расход\n")
            print('Расход записан')
            
        f.write(f"Сумма: {transaction.amount}\n")
        f.write(f"Описание: {transaction.description}\n\n")

def save_transactions(transactions, filename: str):
    # если файл есть, добавим запись
    if filename.is_file():
        write_data_in_file(filename)
            
    # если файла нет, создадим его и добавим запись
    else:
        create_file(filename)
        write_data_in_file(filename)
    
def load_data(filename: str):
    with open(filename, 'r') as file:
        pass
    
