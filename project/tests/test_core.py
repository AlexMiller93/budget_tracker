import unittest

import datetime
from decimal import Decimal
from project.src.budget_tracker.core import Transaction, TransactionType


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.tran_1 = Transaction(
            date=datetime.datetime.now(),
            transaction_type=TransactionType.INCOME,
            amount=Decimal(1000),
            description='foo'
        )

        self.tran_2 = Transaction(
            date=datetime.datetime.now(),
            transaction_type=TransactionType.EXPENSE,
            amount=Decimal(500),
            description='bar'
        )

        self.tran_3 = Transaction(
            date=datetime.datetime.now(),
            transaction_type=TransactionType.EXPENSE,
            amount=Decimal(100),
            description=''
        )

    def test_transaction_type(self):
        self.assertEqual(
            self.tran_1.transaction_type, TransactionType.INCOME)
        self.assertEqual(
            self.tran_2.transaction_type, TransactionType.EXPENSE)

    def test_amount(self):
        self.assertEqual(
            self.tran_1.amount, Decimal('1000'))
        self.assertEqual(
            self.tran_2.amount, Decimal('500'))
        self.assertEqual(
            self.tran_3.amount, Decimal('100'))

    def test_description(self):
        self.assertEqual(
            self.tran_1.description, 'foo')
        self.assertEqual(
            self.tran_2.description, 'bar')
        self.assertEqual(
            self.tran_3.description, '')

    def test_date(self):
        self.assertEqual(
            self.tran_1.date, datetime.datetime.now())
        self.assertEqual(
            self.tran_2.date, datetime.datetime.now())

    def tearDown(self):
        pass

# python -m unittest project.tests.test_core


# if __name__ == '__main__':
#     unittest.main()
