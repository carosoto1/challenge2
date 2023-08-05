from peewee import *
from schemas.card import Card

db = SqliteDatabase('./db/debit_card.db', timeout=10)

class Charge(Model):
    card_id = ForeignKeyField(Card, backref='charges')
    date_time = DateField()
    ammount = FloatField()

    class Meta:
        database = db