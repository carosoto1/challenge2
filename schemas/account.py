from peewee import *
from .user import User

db = SqliteDatabase('./db/debit_card.db', timeout=10)

class Account(Model):
    user_id = ForeignKeyField(User, backref="accounts")
    balance = DecimalField(max_digits=10, decimal_places=2)
    open_date = DateField()
    limit = FloatField()

    class Meta:
        database = db