from schemas.card import Card
from schemas.charge import Charge
from schemas.account import Account

from typing import Union, List

from controllers.account_controller import AccountController
import datetime

class ChargeController:
    #create charge
    @staticmethod
    def create_charge(card:Card, date_time: datetime.datetime, ammount: float) -> Charge:
        account = Account.get(id=card.account_id)
        if ammount > 0:
            card_id = card.id
            charge = Charge(card_id=card_id, date_time=date_time, ammount=ammount)
            AccountController.update_balance(account=account, ammount=ammount)
            charge.save()
            print('Charge saved')
        else:
            print('Invalid ammount')

    #get charge by id
    @staticmethod
    def get_charge_by_id(id: int) -> Union[Charge,None]:
        try:
            return Charge.get(id=id)
        except Charge.DoesNotExist:
            print('charge doesnt exist')
            return None
        
    #get charge by card
    @staticmethod
    def get_charge_by_card(card: Card) -> Union[List,None]:
        try:
            return list(Charge.filter(card_id=card.id))
        except Card.DoesNotExist:
            print('charge doesnt exist')
            return None
        
    #delete charge by card
    @staticmethod
    def delete_charge(charge: Charge):
        charge.delete_instance()