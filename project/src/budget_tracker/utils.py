import datetime
from decimal import Decimal, InvalidOperation

from project.src.budget_tracker.tracker import BudgetTracker


BUDGET_FILE = 'data/budget.txt'


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
1. Вывод баланса: Отображение текущего баланса, а также доходы и расходы.
2. Добавление записи: Добавление новой записи о доходе или расходе.
3. Редактирование записи: Изменение существующих записей о доходах и расходах.
4. Поиск по записям: Поиск записей по категории, дате или сумме.
5. Удаление всех данных: Очистка данных о балансе, доходах и расходах из файла.
6. Выход""")


def input_type() -> bool:
    while True:
        value = input('''Выберите тип транзакции доход или расход. Для этого нажмите (+/-) или (д/р): ''')
        match value:
            case '+' | 'д' | 'Д':
                return True
            case '-' | 'р' | 'Р':
                return False
            case _:
                print(f"""
    {value} не является типом, введите корректное значение""")


def input_date() -> datetime.date:
    while True:
        value = input('Введите дату (дд.мм.гггг): ')
        try:
            date = datetime.datetime.strptime(value, '%d.%m.%Y')
            return date
        except ValueError:
            print(f"{value} не является датой, введите корректное значение")


def input_amount() -> Decimal:
    while True:
        value = input('Введите сумму: ')
        try:
            amount = Decimal(value)
            return amount
        except InvalidOperation:
            print(f"{value} не является числом, введите корректное значение")


def input_description():
    value = input('Введите описание: ')
    return value.strip()


def input_index(max_index: int) -> int:
    while True:
        value = input(f'''
            Введите номер транзакции (целое число, от 0 до {max_index}): ''')
        try:
            index = int(value)
            if index < 0:
                raise ValueError(f'{index} меньше нуля')
            if index > max_index:
                raise ValueError(f'{index} больше {max_index}')
            return index
        except ValueError:
            print(f"{value} не является корректным значением")
