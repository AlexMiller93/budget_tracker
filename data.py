from datetime import datetime
from decimal import Decimal, InvalidOperation
import os
from core import BudgetPersistence, Transaction, TransactionType


class FilePersistence(BudgetPersistence):
    """ Класс для работы с данными по транзакциям """

    _DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def read_transactions(self) -> list[Transaction]:
        """ Метод для чтения транзакций """

        data = self._read_data()
        return data

    def add_transaction(self, transaction: Transaction) -> None:
        """ Метод для добавления транзакций """

        line = self._format_transaction(transaction)
        with open(self._file_path, 'at', encoding='utf-8') as f:
            f.write(line + '\n')

    def update_transaction(self, index: int, transaction: Transaction) -> None:
        """ Метод для изменения транзакций """

        transactions = self._read_data()
        transactions[index] = transaction
        self._write_data(transactions)

    def _read_data(self) -> list[Transaction]:
        if not os.path.isfile(self._file_path):
            return []

        data = []
        with open(self._file_path, 'rt', encoding='utf-8') as f:
            for line in f:
                if not line:
                    continue
                tran = self._parse_transaction(line)
                if tran is None:
                    continue
                data.append(tran)
        return data

    def _write_data(self, transactions: list[Transaction]) -> None:
        with open(self._file_path, 'wt', encoding='utf-8') as f:
            for tran in transactions:
                line = self._format_transaction(tran)
                f.write(line + '\n')

    def _format_transaction(self, transaction: Transaction) -> str:
        transaction.date = datetime.now()
        date_str = transaction.date.strftime(self._DATE_FORMAT)
        text = f"""
            {date_str}\t{transaction.transaction_type.value}\t
            {transaction.amount}\t{transaction.description}"""
        return text

    def _parse_transaction(self, raw_data: str) -> Transaction | None:
        # разбиваем данные на 4 части
        parts = raw_data.split('\t', maxsplit=3)

        # если
        if len(parts) != 4:
            return None

        # обработка даты
        try:
            tran_date = datetime.datetime.strptime(
                parts[0], self._DATE_FORMAT)
        except ValueError:
            return None

        # обработка кода транзакции
        try:
            tran_type_code = int(parts[1])
        except ValueError:
            return None

        # обработка типа транзакции
        try:
            tran_type = TransactionType(tran_type_code)
        except ValueError:
            return None

        # обработка количества денег в транзакции
        try:
            tran_amount = Decimal(parts[2])
        except InvalidOperation:
            return None

        tran_desc = parts[3].replace('\t', ' ')

        # возвращаем объект транзакции
        return Transaction(
            date=tran_date,
            transaction_type=tran_type,
            amount=tran_amount,
            description=tran_desc
        )
