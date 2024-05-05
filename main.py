from datetime import datetime
from utils import (
    clean_data_in_file, 
    handle_int_input,
    save_transactions,
    search_data)

from core import BudgetTracker, Transaction

BUDGET_FILE = 'data/budget.txt'

if __name__ == '__main__':
    # todo: добавить логику для обновления баланса, а не обнуления после каждого запуска
    budget_tracker = BudgetTracker()
    
    print("\nДобро пожаловать в твой личный финансовый кошелек!")
    
    while True:
        
        print(""" 
Вам доступен следующий функционал: 

1. Вывод баланса: Отображение текущего баланса, а также отдельно доходы и расходы.
2. Добавление записи: Добавление новой записи о доходе или расходе.
3. Редактирование записи: Изменение существующих записей о доходах и расходах.
4. Поиск по записям: Поиск записей по категории, дате или сумме.
5. Удаление всех данных: Очистка данных о балансе, доходах и расходах из файла.
6. Выход
            """)
        
        choice = int(input("Выберите цифру (1/2/3/4/5/6): "))
        match choice:
            
            #* Вывод баланса
            case 1:
                
                print(f"""
    Текущий баланс: {budget_tracker.balance}\n
    Доходы: {budget_tracker.incomes}\n
    Расходы: {budget_tracker.expenses}\n
                    """)
                
            #* Добавление записи
            case 2:
                
                # создание пустой транзакции
                transaction = Transaction()
                category = input('Выберите категорию доход или расход (+/-) или (д/р): ')
                
                #* Занесение данных о доходе
                if category == '+' or category == 'д':
                    value = handle_int_input()
                    
                    transaction.type = 'Income'
                    transaction.amount = value
                    
                    budget_tracker.balance += value
                    budget_tracker.incomes += value
                    
                    transaction.date = datetime.now().strftime('%Y-%m-%d')
                    
                    description = input('Добавьте описание: ')
                    transaction.description = description
                    
                    budget_tracker.transaction = transaction
                    
                    # запись данных в файл
                    save_transactions(BUDGET_FILE, transaction)
                    
                # Занесение данных о расходе
                elif category == '-' or category == 'р':
                    value = handle_int_input()
                    
                    transaction.type = ''
                    transaction.amount = value
                    
                    budget_tracker.balance -= value
                    budget_tracker.expenses += value
                
                    transaction.date = datetime.now().strftime('%Y-%m-%d')
                    
                    description = input('Добавьте описание: ') 
                    transaction.description = description
                    
                    budget_tracker.transaction = transaction
                    
                    # запись данных в файл
                    save_transactions(BUDGET_FILE, transaction)
                    
                else:
                    print('Некорректный выбор. Выберите категорию доход или расход (+/-) или (д/р)')
                    
                budget_tracker.transactions = transaction
                
            #? Редактирование записи
            case 3:
                # Категория, Сумма, Описание
                
                print(""" 
    Выберите какое поле вы хотите изменить: 

    1. Категория: доход/расход.
    2. Сумма.
    3. Описание
                """)
                choice = input("Выберите цифру (1/2/3): ")
                match choice:
                    
                    # замена категории
                    case 1:
                        category = input('Выберите категорию доход или расход (+/-) или (д/р): ')
                        
                        if category == '+' or category == 'д':
                            search_data(BUDGET_FILE, category)
                            
                        elif category == '-' or category == 'р':
                            search_data(BUDGET_FILE, category)
                            
                    # замена суммы
                    case 2:
                        pass
                    
                    # замена описания
                    case 3:
                        pass
                    
                    case _:
                        print('Некорректный выбор. Выберите цифру из предложенных вариантов (1/2/3)')
                
            
            # *Поиск по записям
            case 4:
                target = input('Введите что вы хотите найти (категория, сумма, описание, дата): ')
                search_data(BUDGET_FILE, target)
                # todo: добавить подсветку слова в файле
            
            #* Удаление данных из файла
            case 5:
                clean_data_in_file(BUDGET_FILE)
                
            #* Выход из программы
            case 6:
                # todo: добавить логику при выходе, 
                # todo: сохранить данные о бюджете или все очистить
                
                print("""
    Удалить данные о балансе, доходах и расходах или оставить?

    1. Удалить данные: 
    2. Оставить данные:
                    """)
                
                data_choice = int(input("Выберите цифру (1/2): "))
                match data_choice:
                    case 1:
                        budget_tracker = BudgetTracker()
                        break
                    
                    case 2:
                        # оставить данные о балансе и пр.
                        pass
                    
                    case _:
                        print('Некорректный выбор. Выберите цифру из предложенных вариантов (1/2)')
            
            case _:
                print('Некорректный выбор. Выберите цифру из предложенных вариантов (1/2/3/4/5/6)')
        