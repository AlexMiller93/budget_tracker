
import datetime
from core import TransactionType
from tracker import BudgetTracker
from utils import (
    input_amount,
    input_date,
    input_description,
    input_index,
    input_type)

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def add_transaction(tracker: BudgetTracker) -> None:
    """ Функция для добавления транзакции в трекер по введенным параметрам:
        дата, сумма или описание. Добавляет транзакцию в файл.
    """

    # выбираем тип транзакции
    is_income = input_type()
    amount = input_amount()
    desc = input_description()
    date = datetime.date.today()

    # если добавляем доход
    if is_income:
        tracker.add_income(date=date, amount=amount, description=desc)
        print('Данные о доходе записаны!')

    # если добавляем расход
    else:
        tracker.add_expense(date=date, amount=amount, description=desc)
        print('Данные о расходе записаны!')


def edit_transaction(tracker: BudgetTracker) -> None:
    """ Функция для изменения транзакции по введенным параметрам:
        дата, сумма или описание. Обновляет транзакцию в файле.
    """

    # получаем количество текущих транзакций
    tran_count = tracker.get_count()
    if tran_count == 0:
        print('Нет ни одной транзакции')
    index = input_index(tran_count - 1)

    while True:
        target = input('''
Укажите, что изменить: дата (1), сумма (2), описание (3): ''')
        params = None
        match target:
            case '1':
                date = input_date()
                params = {
                    'date': date
                }
                break
            case '2':
                amount = input_amount()
                params = {
                    'amount': amount
                }
                break
            case '3':
                desc = input_description()
                params = {
                    'description': desc
                }
                break
            case _:
                print(f'{target} неизвестно, введите корректное значение')

    # обновляем транзакцию по введенным параметрам
    tracker.update(index=index, **params)
    print('Транзакция изменена')


def search(tracker: BudgetTracker) -> None:
    """ Функция для поиска транзакции по введенным параметрам.
        Выводит одну транзакцию или несколько, если находит по параметрам"""

    while True:
        search_params = None
        target = input('''Укажите, по каким параметрам искать
                    (тип транзакции (1), дата (2), сумма (3)): ''')
        match target:

            case '1':
                is_income = input_type()
                search_params = {
                    'is_income': is_income
                }
                break
            case '2':
                date = input_date()
                search_params = {
                    'date': date
                }
                break
            case '3':
                amount = input_amount()
                search_params = {
                    'amount': amount
                }
                break
            case _:
                print(f'{target} неизвестно, введите корректное значение')

    matching_transactions = tracker.search(**search_params)
    if len(matching_transactions) == 0:
        print('Данных, соответствующих критериям, не найдено!')
    else:
        print('Найдены транзакции:')
        for (idx, tran) in matching_transactions:
            type_name = 'доход' if tran.type == TransactionType.INCOME else 'расход'
            date_str = tran.date.strftime('%d.%m.%Y')
            print(f'Транзакция №{idx}')
            print(f'- тип: {type_name}')
            print(f'- дата: {date_str}')
            print(f'- сумма: {tran.amount}')
            print(f'- описание: {tran.description}')
            print()


def clear_data(tracker: BudgetTracker) -> None:
    """ Функция для очистки данных по транзакциям с трекера """

    while True:
        choice = input('Вы точно хотите очистить данные с трекера? y/n: ')
        match choice:
            case 'y' | 'Y':
                tracker.clear()
                print('Данные с трекера удалены!')
            case 'n' | 'N':
                return
            case _:
                print('Некорректный выбор. Нажмите y или n')
