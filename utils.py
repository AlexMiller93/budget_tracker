import os
from typing import Type

from core import Transaction
from tracker import BudgetTracker


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
        
def write_data_in_file(filename: str, transaction: Type[Transaction]): 
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"Дата: {transaction.date}\n")
        
        if transaction.type == 'Income':
            f.write(f"Категория: Доход\n")
            print('Доход записан')
        else:
            f.write(f"Категория: Расход\n")
            print('Расход записан')
            
        f.write(f"Сумма: {transaction.amount}\n")
        
        if transaction.description:
            f.write(f"Описание: {transaction.description}\n\n")
        else:
            f.write(f"Описание: ---\n\n")

def save_transactions(filename: str, transaction: Type[Transaction]):
    # если файл есть, добавим запись
    if os.path.isfile(filename):
        write_data_in_file(filename, transaction)
            
    # если файла нет, создадим его и добавим запись
    else:
        create_file(filename)
        write_data_in_file(filename, transaction)
    
def search_data(filename: str, target: str):
    with open(filename, 'r') as file:
        text = file.read()
        if target in text:
            print(f'Слово {target} найдено')
            return True
        print(f'Слова {target} нет')
        return False
            
def replace_word_in_file(filename: str, old_word: str, new_word: str):
    with open(filename, 'r+', encoding='utf-8') as file:
        text = file.read()
        
        words = text.split()
        if old_word in words:
            text = text.replace(old_word, new_word)
            file.seek(0)
            file.write(text)
            file.truncate()
            print(f'В файле заменено {old_word} {new_word}')

def clean_data_in_file(filename: str): 
    open(filename, 'w').close()
    print('Файл очищен')

def display_balance(tracker: BudgetTracker) -> None:
    balance = tracker.get_balance()
    income = tracker.get_total_income()
    expenses = tracker.get_total_expenses()
    print(f"""
Текущий баланс: {balance}
Доходы: {income}
Расходы: {expenses}
    """)
    
def display_menu() -> None:
    print("""
\nВам доступен следующий функционал:
1. Вывод баланса: Отображение текущего баланса, а также отдельно доходы и расходы.
2. Добавление записи: Добавление новой записи о доходе или расходе.
3. Редактирование записи: Изменение существующих записей о доходах и расходах.
4. Поиск по записям: Поиск записей по категории, дате или сумме.
5. Удаление всех данных: Очистка данных о балансе, доходах и расходах из файла.
6. Выход""")
    


# clean_data_in_file(BUDGET_FILE)
# replace_word_in_file(BUDGET_FILE, '400', '500')