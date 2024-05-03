import click

@click.command(help="Вывод баланса, доходов и расходов")
@click.argument("value", type=click.INT)
def get_balance(value):
    # Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.
    pass

@click.command()
def add_note():
    # params: доход/расход кол-во описание=None
    pass

@click.command()
def edit_note():
    #? params: доход/расход кол-во описание + дата
    pass

@click.command()
def search():
    #? params: доход/расход кол-во описание + дата
    pass