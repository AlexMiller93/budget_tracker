from decimal import Decimal
import os
from typing import Type

from core import Transaction
from tracker import BudgetTracker


BUDGET_FILE = 'data/budget.txt'


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
\nВам доступен следующий функционал:\n
1. Вывод баланса: Отображение текущего баланса, а также отдельно доходы и расходы.
2. Добавление записи: Добавление новой записи о доходе или расходе.
3. Редактирование записи: Изменение существующих записей о доходах и расходах.
4. Поиск по записям: Поиск записей по категории, дате или сумме.
5. Удаление всех данных: Очистка данных о балансе, доходах и расходах из файла.
6. Выход""")
    
def handle_amount() -> Decimal:
    while True:
        value = input('Введите сумму: ')
        
        try:
            amount = Decimal(value=value, context=None)
            break
        except ValueError:
            pass
        
    return amount

# clean_data_in_file(BUDGET_FILE)
# replace_word_in_file(BUDGET_FILE, '400', '500')