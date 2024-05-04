from datetime import datetime
from utils import handle_int_input, write_data_in_file
from core import BudgetTracker, Transaction

BUDGET_FILE = 'data/budget.txt'

if __name__ == '__main__':
    # todo: добавить логику для обновления баланса, а не обнуления после каждого запуска
    budget_tracker = BudgetTracker()
    
    print("Добро пожаловать в твой личный финансовый кошелек!")
    
    while True:
        
        print(""" 
Доступны следующие функции: 

1. Вывод баланса: Отображение текущего баланса, а также отдельно доходы и расходы.
2. Добавление записи: Добавление новой записи о доходе или расходе.
3. Редактирование записи: Изменение существующих записей о доходах и расходах.
4. Поиск по записям: Поиск записей по категории, дате или сумме.
5. Выход
            """)
        
        choice = input("Выберите цифру (1/2/3/4/5): ")
        
        #* Вывод баланса
        if choice == '1':
            
            print(f"""
Текущий баланс: {budget_tracker.balance}\n
Доходы: {budget_tracker.incomes}\n
Расходы: {budget_tracker.expenses}\n
                """)
            
        #* Добавление записи
        elif choice == '2':
            
            # создание пустой транзакции
            transaction = Transaction()
            category = input('Выберите категорию доход или расход (in/ex): ')
            
            # Занесение данных о доходе
            if category == 'in':
                value = handle_int_input()
                
                transaction.type = 'Income'
                transaction.amount = value
                
                budget_tracker.balance += value
                budget_tracker.incomes += value
                
                transaction.date = datetime.now().strftime('%Y-%m-%d')
                
                description = input('Добавьте описание: ')
                transaction.description = description
                
                # запись данных в файл
                write_data_in_file(BUDGET_FILE, transaction)
                
            # Занесение данных о расходе
            elif category == 'ex':
                value = handle_int_input()
                
                transaction.type = 'Expense'
                transaction.amount = value
                
                budget_tracker.balance -= value
                budget_tracker.expenses += value
            
                transaction.date = datetime.now().strftime('%Y-%m-%d')
                
                description = input('Добавьте описание: ')
                transaction.description = description
                
                # запись данных в файл
                write_data_in_file(BUDGET_FILE, transaction)
                
            else:
                print('Некорректный выбор. Выберите категорию доход или расход (in/ex)')
                
            budget_tracker.transactions = transaction
        # Редактирование записи
        elif choice == '3':
            pass
        
        # Поиск по записям
        elif choice == '4':
            pass
        
        elif choice == '5':
            break
        
        else:
            print('Некорректный выбор. Выберите цифру из предложенных вариантов (1/2/3/4/5)')
        