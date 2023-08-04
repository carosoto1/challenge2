import datetime
from db.migrations import create_db

from schemas.user import User
from schemas.account import Account
from schemas.card import Card

from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController


if __name__ == "__main__":
    create_db('db/debit_card.db')
    user = UserController.create_user(age=60, name='caro soto')
    account = AccountController.create_account(user=user, balance=0, open_date=datetime.datetime.now(), limit=50000)
    CardController.create_card(account=account,cvv=123, user=user)
 
    #UserController.delete_user(UserController.get_user_by_id(id=2))
    #AccountController.update_limit(account, 2000)
    #print(UserController.get_user_by_id(name= 'caro soto').name)
    
    for i in Account.select():
        print(i.id, i.user_id, i.balance, i.open_date, i.limit)

    for i in User.select():
        print(i.id, i.age, i.name)

    for i in Card.select():
        print(i.id,i.account_id, i.name, i.cvv)

    for i in User.select():
        print(i.id)