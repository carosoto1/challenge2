import datetime
from db.migrations import create_db

from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.charge import Charge
from schemas.payment import Payment

from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.charge_controller import ChargeController
from controllers.payment_controller import PaymentController

if __name__ == "__main__":

    create_db('db/debit_card.db')

    user = UserController.create_user(age=60, name='caro soto')
    print(UserController.get_user_by_name(name='caro soto').name)
    #UserController.delete_user(UserController.get_user_by_id(id=2))

    account = AccountController.create_account(user=user, balance=0, open_date=datetime.datetime.now(), limit=50000)
    print(AccountController.get_account_by_user(user=user))
    #AccountController.update_limit(account, 2000)

    card = CardController.create_card(account=account,cvv=123, user=user)
    print(list(CardController.get_card_by_account(account=account)))

    charge = ChargeController.create_charge(card=card, date_time=datetime.datetime.now(), ammount=12000)
    print(list(ChargeController.get_charge_by_card(card=card)))
    
    payment= PaymentController.create_payment(account=account, date_time=datetime.datetime.now(), ammount=2000)
    print(PaymentController.get_payment_by_account(account=account))
    
    # for i in Account.select():
    #     print(i.id, i.user_id, i.balance, i.open_date, i.limit)

    # for i in User.select():
    #     print(i.id, i.age, i.name)

    # for i in Card.select():
    #     print(i.id,i.account_id, i.name, i.cvv)

    # for i in User.select():
    #     print(i.id)