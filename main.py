from project.src.budget_tracker.commands import (
    add_transaction,
    clear_data,
    edit_transaction,
    search)
from project.src.budget_tracker.data import FileStorage

from project.src.budget_tracker.tracker import BudgetTracker
from project.src.budget_tracker.utils import display_balance, display_menu

BUDGET_FILE = 'data/budget.txt'


def main():
    storage = FileStorage(BUDGET_FILE)
    tracker = BudgetTracker(storage)

    print("\nДобро пожаловать в твой личный финансовый кошелек!")
    while True:
        display_menu()

        choice = input("\nВведите цифру (1/2/3/4/5/6): ").strip()

        match choice:
            case '1':
                display_balance(tracker)
            case '2':
                add_transaction(tracker)
            case '3':
                edit_transaction(tracker)
            case '4':
                search(tracker)
            case '5':
                clear_data(tracker)
            case '6':
                break
            case _:
                print('\nНекорректный выбор. Введите цифру (1/2/3/4/5/6)')

    print("\nДо свидания!\n")


if __name__ == '__main__':
    main()
