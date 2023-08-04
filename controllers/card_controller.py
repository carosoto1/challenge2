from schemas.account import Account, User
from schemas.card import Card
from typing import Union
import datetime

#from typing import 

class CardController:
    @staticmethod
    def create_card(
        account: Account,
        cvv: str,
        user: User
    )-> Card:
        card = Card(account_id=account.id, name=user.name, cvv=cvv)
        card.save()
        return card  
    

    #get card
    @staticmethod
    def get_card_by_id(id: int) -> Union[Card, None]:
        try:
            return Card.get(id=id)
        except Card.DoesNotExist:
            return None
        
    #get card by account
    @staticmethod
    def get_card_by_account(account: Account) -> Union[Card, None]:
        try:
            return Card.filter(account_id=account.id)
        except Card.DoesNotExist:
            return None

    #update card
    @staticmethod
    def update_card(card: Card):
        card.limit = card
        card.save()
        return card

    #delete card
    @staticmethod
    def delete_card(card: Card):
        account = Account.get(id = account.id)
        balance = account.balance
        if balance == 0:
            card.delete_instance()
            print('Card deleted')
        else:
            print('Cant delete card, balance is not 0')