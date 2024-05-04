import click

from core import Budget


@click.command(help="Вывод функционала программы")
def show_menu():
    pass

@click.group()
def finance():
    pass


@finance.command(help="Вывод баланса, доходов и расходов")
def get_balance(value):
    # Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.
    pass


@finance.command(help="Добавление записи о доходах и расходах")
@click.option('--category', prompt='Введите категорию', help='Категория дохода или расхода')
@click.option('--income/--expenses', default=True)
@click.argument('amount', type=int)
@click.option('--description', prompt='Введите описание', help='Описание дохода или расхода')
def add_note(income, amount):
    # params: доход/расход кол-во описание=None
    budget_note = Budget() 
    click.echo('Запись создана')
    
    if income:
        budget_note.balance += amount
        budget_note.income += amount
        click.echo('Доходы добавлены')
        
    budget_note.balance -= amount
    budget_note.expenses += amount
    click.echo('Расходы добавлены')
    
    

@finance.command(help="Изменение записи, баланса, доходов и расходов")
def edit_note():
    #? params: доход/расход кол-во описание
    pass

@finance.command(help="Поиск по дате, балансу, по значению")
def search():
    #? params: доход/расход кол-во описание + дата
    pass