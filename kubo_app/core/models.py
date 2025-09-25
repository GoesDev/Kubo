from .constants import ACCOUNT_TYPE

class User():

    def __init__(self, name, email, password):
        
        self.name = name
        self.email = email
        self.password = password
        self.login_mode = 'online'

class Account():

    def __init__(self, name, balance, account_type_key):
        
        self.name = name
        self.current_balance = balance
        self.account_type = ACCOUNT_TYPE[account_type_key]
    
    def display_account(self):
        print(self.name, self.balance, self.account_type)