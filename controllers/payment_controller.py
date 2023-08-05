from schemas.card import Card
from schemas.charge import Charge
from schemas.account import Account
from schemas.payment import Payment

from typing import Union, List

from controllers.account_controller import AccountController
import datetime

class PaymentController:
    #create payment
    @staticmethod
    def create_payment(account:Account, date_time: datetime.datetime, ammount: float):
        ammount = -ammount
        if (AccountController.update_balance(account=account, ammount=ammount)) & (ammount<0):
            account_id = account.id
            payment = Payment(account_id=account_id,date_time=date_time, ammount=ammount)
            payment.save()
            print(f'Payment saved: {account_id}')
            return payment
        else:
            print('Payment failed')

    #get payment by id
    @staticmethod
    def get_payment_by_id(id: int) -> Union[Payment,None]:
        try:
            return Payment.get(id=id)
        except Payment.DoesNotExist:
            print('Payment doesnt exist')
            return None
        
    #get payment by account
    @staticmethod
    def get_payment_by_account(account: Account) -> Union[List,None]:
        try:
            return list(Payment.filter(account_id=account.id))
        except Payment.DoesNotExist:
            print('Payment doesnt exist')
            return None
        
    #delete payment
    @staticmethod
    def delete_payment(payment: Payment):
        payment.delete_instance()