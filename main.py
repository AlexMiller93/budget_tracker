import argparse
from commands import get_balance, edit_note, add_note, search_note


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Учет личных доходов и расходов')

    parser.add_argument(
        '--balance', 
        help='Показать текущий баланс', 
        action='store_true')
    
    parser.add_argument(
        '--add', 
        help='Добавить запись о доходе или расходе', 
        action='store_true')
    
    parser.add_argument(
        '--edit', 
        help='Изменить запись о доходе или расходе', 
        action='store_true')
    
    parser.add_argument(
        '--search', 
        help='Поиск записей по категории, дате или сумме', 
        action='store_true')

    args = parser.parse_args()

    if args.balance:
        get_balance()
    elif args.add:
        add_note()
    elif args.edit:
        edit_note()
    elif args.search:
        search_note()
    else:
        parser.print_help()