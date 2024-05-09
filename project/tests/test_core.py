import unittest

import datetime
from decimal import Decimal
from project.src.budget_tracker.core import Transaction, TransactionType


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.tran_1 = Transaction(
            date=datetime.datetime.now(),
            transaction_type=TransactionType.INCOME,
            amount=Decimal('1000'),
            description='foo'
        )

        self.tran_2 = Transaction(
            date=datetime.datetime.now(),
            transaction_type=TransactionType.EXPENSE,
            amount=Decimal('500'),
            description='bar'
        )

    def test_type(self):
        self.assertEqual(
            self.tran_1.transaction_type == TransactionType.INCOME)
        self.assertEqual(
            self.tran_2.transaction_type == TransactionType.EXPENSE)

    def tearDown(self):
        pass


# if __name__ == '__main__':
#     unittest.main()
