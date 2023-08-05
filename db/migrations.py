import os
import time
from peewee import SqliteDatabase
from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.charge import Charge
from schemas.payment import Payment

def create_db(path: str):
    if not os.path.isfile(path):
        db = SqliteDatabase(path)
        time.sleep(1)
        db.create_tables([User, Account, Card, Charge, Payment])
        return True