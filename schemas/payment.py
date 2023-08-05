from peewee import *
from schemas.account import Account

db = SqliteDatabase('./db/debit_card.db', timeout=10)

class Payment(Model):
    account_id = ForeignKeyField(Account, backref='charges')
    date_time = DateField()
    ammount = FloatField()

    class Meta:
        database = db