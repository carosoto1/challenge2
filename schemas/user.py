from peewee import *

db = SqliteDatabase('./db/debit_card.db', timeout=10)

class User(Model):
    age = IntegerField()
    name = CharField()

    class Meta:
        database = db