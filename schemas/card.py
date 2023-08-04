from peewee import *
from .account import Account

db = SqliteDatabase('./db/debit_card.db', timeout=10)

class Card(Model):
    account_id = ForeignKeyField(Account, backref="cards")
    name = CharField()
    cvv = CharField(max_length=3)

    class Meta:
        database = db