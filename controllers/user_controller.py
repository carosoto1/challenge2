from schemas.user import User
from schemas.account import Account
from controllers.account_controller import AccountController

class UserController:
    @staticmethod
    def create_user(age: int, name: str) -> User:
        user = User(age=age, name=name)
        user.save()
        return user
    
    #get users
    @staticmethod
    def get_user() -> User:
        return User
    
    #get user by id
    @staticmethod
    def get_user_by_id(id: int) -> User:
        return User.get(id=id)
       
    #get user by name
    @staticmethod
    def get_user_by_name(name: str) -> User:
        return User.get(name=name)
    
    #update user
    @staticmethod
    def update_user(user: User, name: str) -> User:
        user.name = name
        user.save()
        return user
    
    #delete user
    @staticmethod
    def delete_user(user: User):
        try:
            account = Account.get(user_id = user.id)
        except:
            account = None
        if account is None:
            user.delete_instance()
        else:
            AccountController.delete_account(account = account)
            user.delete_instance()
            print('User Deleted')