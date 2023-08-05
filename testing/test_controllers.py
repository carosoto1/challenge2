import datetime
from peewee import SqliteDatabase
import unittest

from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.charge import Charge
from schemas.payment import Payment

from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController

db = SqliteDatabase('db/debit_card.db')

class TestModels(unittest.TestCase):
    def setUp(self):
        db.bind([User, Account, Card, Charge, Payment])
        db.connect()
        db.create_tables([User, Account, Card, Charge, Payment])

    def tearDown(self):
        db.drop_tables([User, Account, Card, Charge, Payment])
        db.close()

    def test_create_user(self):
        user = UserController.create_user(age=60, name='caro soto')
        self.assertEqual(User.select().count(), 1)

    def test_create_account(self):
        account = AccountController.create_account(user=User, balance=0, open_date=datetime.datetime.now(), limit=50000)
        self.assertEqual(Account.select().count(), 1)

    def test_create_card(self):
        card = CardController.create_card(account=Account,cvv=123, user=User)
        self.assertEqual(Card.select().count(), 1)