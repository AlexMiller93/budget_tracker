from commands import (
    add_transaction, 
    clear_data, 
    edit_transaction, 
    search)
from data import FilePersistence

from core import BudgetTracker
from utils import display_balance, display_menu

BUDGET_FILE = 'data/budget.txt'


def main():
    persistence = FilePersistence(BUDGET_FILE)
    tracker = BudgetTracker(persistence)
    
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
            
    print("До свидания!")
    
if __name__ == '__main__':
    main()
    