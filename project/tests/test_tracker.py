import datetime
from decimal import Decimal
import unittest

from project.src.data import BudgetTracker
from project.src.budget_tracker.core import Transaction


class TestBudgetTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = BudgetTracker()

    def test_add_income(self):

        self.tracker.add_income(
            date=datetime.datetime.now(),
            amount=Decimal(1000),
            description='тест доход')

        self.assertEqual(self.tracker.get_total_income(), '1000')

    def test_add_expense(self):
        self.tran_1 = Transaction(
            date=datetime.datetime.now(),
            amount=Decimal(1000),
            description='тест расход'
        )

        self.tracker.add_expense(
            date=datetime.datetime.now(),
            amount=Decimal(100),
            description='тест доход')
        self.assertEqual(self.tracker.get_total_expenses(), '100')

    def test_get_total_income(self):
        pass

    def test_get_total_expense(self):
        pass

    def test_get_total_balance(self):
        pass

    def test_clear(self):
        pass

    def test_get_count(self):
        pass

    def tearDown(self):
        pass
