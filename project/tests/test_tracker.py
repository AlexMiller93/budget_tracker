import datetime
from decimal import Decimal
import unittest

from project.src.budget_tracker.data import FileStorage
from project.src.budget_tracker.tracker import BudgetTracker


class TestBudgetTracker(unittest.TestCase):
    def setUp(self):
        self.file_path = 'data/test.txt'
        self.storage = FileStorage(self.file_path)
        self.tracker = BudgetTracker(self.storage)

    def test_add_income(self):
        self.tracker.add_income(
            date=datetime.datetime.now(),
            amount=Decimal(1000),
            description='тест доход')

        self.assertEqual(
            self.tracker.get_balance(), Decimal('1000'))

    def test_add_expense(self):
        self.tracker.add_expense(
            date=datetime.datetime.now(),
            amount=Decimal(100),
            description='тест расход')
        self.assertEqual(
            self.tracker.get_balance(), Decimal('-100'))

    def test_get_total_income(self):
        self.tracker.add_income(
            date=datetime.datetime.now(),
            amount=Decimal(500),
            description='тест доход')

        self.assertEqual(self.tracker.get_total_income(), Decimal('500'))

    def test_get_total_expense(self):
        self.tracker.add_expense(
            date=datetime.datetime.now(),
            amount=Decimal(200),
            description='тест расход')
        self.assertEqual(self.tracker.get_total_expenses(), Decimal('200'))

    def test_get_total_balance(self):
        self.tracker.add_income(
            date=datetime.datetime.now(),
            amount=Decimal(600),
            description='тест доход')

        self.tracker.add_expense(
            date=datetime.datetime.now(),
            amount=Decimal(300),
            description='тест расход')
        self.assertEqual(self.tracker.get_balance(), Decimal('300'))

    def test_clear(self):
        self.tracker.clear()
        self.assertEqual(self.tracker.get_balance(), Decimal('0'))

    def test_update_amount(self):
        self.tracker.add_income(
            date=datetime.datetime.now(),
            amount=Decimal(400),
            description='тест доход')

        self.tracker.add_expense(
            date=datetime.datetime.now(),
            amount=Decimal(300),
            description='тест расход')

        self.tracker.update(
            index=0,
            amount=Decimal(500),
        )
        self.assertEqual(self.tracker.get_balance(), Decimal('200'))

    def test_update_date(self):
        self.tracker.add_income(
            date=datetime.datetime.now(),
            amount=Decimal(100),
            description='тест доход')

        self.tracker.update(
            index=0,
            date=datetime.datetime.now(),
        )
        self.assertEqual(self.tracker.get_balance(), Decimal('100'))

    def test_search_income(self):
        self.tracker.add_income(
            date=datetime.datetime.now(),
            amount=Decimal(1000),
            description='тест доход')

        self.tracker.add_expense(
            date=datetime.datetime.now(),
            amount=Decimal(300),
            description='тест расход')

        self.tracker.search(is_income=True)
        self.assertEqual(self.tracker.get_balance(), Decimal('700'))

    def tearDown(self):
        self.tracker.clear()

# python -m unittest project.tests.test_tracker
