## Консольное приложение "Личный финансовый кошелек"

### Установка приложения

Нужно склонировать проект на локальную машину

``` git clone https://github.com/AlexMiller93/budget_tracker.git ```

Для запуска приложения необходимо запустить файл main.py

``` python main.py ```

### Основные возможности приложения

1. Вывод баланса: Показать текущий баланс, а также доходы и расходы.
2. Добавление записи: Возможность добавления новой записи в текстовый файл о доходе или расходе.
3. Редактирование записи: Изменение существующих записей в файле о доходах и расходах.
4. Поиск по записям: Поиск записей по категории, дате или сумме.
5. Удаление всех данных: Очистка данных в файле о балансе, доходах и расходах.

### Описание функционала приложения

Модули программы расположены в папке project\src\budget_tracker.

В модуле core.py находятся классы Transaction для создания транзакций, TransactionType для определения типа транзакции (доход/расход), а также абстрактный класс BudgetStorage для взаимодействия с транзакциями.

В модуле tracker.py находится класс BudgetTracker для хранения данных с транзакциями и балансе, а также для совершения операций с транзакциями.

В классе BudgetTracker есть множество публичных и приватных методов для работы с транзакциями, к примеру add_income для добавления дохода или метод search для поиска транзакции по введенным параметрам.

В модуле data.py находится класс FileStorage для взаимодействия с транзакциями, который наследуется от абстрактного класса BudgetStorage.

В классе реализованы методы для CRUD операций с транзакциями, а именно add_transaction, read_transactions, update_transaction, delete_transactions.

В модуле utils.py находятся функции ввода различных типов данных для создания или обновления транзакций.

В модуле commands.py находятся функции основные функции приложения, такие как add_transaction, update_transaction, search, clear_data.

В главном модуле main.py, находящимся в корне проекта, находится  функция для запуска
приложения main.

В папке project\tests находятся тесты для приложения.

В модуле test_core.py написаны тесты по транзакциям, в модуле test_tracker.py тесты для трекера транзакций.

В файле data\budget.txt находится пример текстового файла с данными по транзакциям.
