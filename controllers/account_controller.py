from schemas.account import Account, User
from schemas.card import Card
from typing import Union
import datetime

#from typing import 

class AccountController:
    @staticmethod
    def create_account(
        user: User,
        balance: float,
        open_date: datetime.datetime,
        limit: float
    ):
        account = Account(user_id=user.id, balance=balance, open_date=open_date, limit=limit)
        account.save()
        return account

    #get account by id
    @staticmethod
    def get_account_by_id(id: int) ->Account:
        return Account.get(id=id)
    
    #get account by user
    @staticmethod
    def get_account_by_user(user: User)-> Union[Account,None]:
        try:
            return Account.get(user_id=user.id)
        except Account.DoesNotExist:
            return None
        
    #get account by card
    @staticmethod
    def get_account_by_card(card: Card)-> Account:
        return Card.get(id=card.account_id)
    
    #update balance
    @staticmethod
    def update_balance(account: Account,amount: float) -> bool:
        balance = account.balance + amount
        account.balance = balance
        account.save()
        return True

    #update limit
    @staticmethod
    def update_limit(account: Account,limit: int):
        account.limit = limit
        account.save()
        return account

    #delete account
    @staticmethod
    def delete_account(account: Account):
        try:
            card = Account.get(account_id = account.id)
        except:
            card = None
        if card is None:
            account.delete_instance()
        else:
            card.delete_instance()
            account.delete_instance()
            print('Account and Cards deleted')
