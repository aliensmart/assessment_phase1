from .orm import ORM
import random





class Account(ORM):
    tablename = "accounts"
    fields = ["username", "pin", "balance", "api_key"]

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.username = kwargs.get("username")
        self.pin = kwargs.get("pin")
        self.balance = kwargs.get("balance")
        self.api_key = None

    #instance 
    # method instance.generate_api_key() 
    # for the Account
    def generate_api_key(self):
        """
        This method sets the  self.api_key 
        property to a random string of at least 20 
        numbers or characters

        """
        start = 10**19
        end = (10**20)-1
       
        new_api = random.randint(start,end)
        self.api_key = str(new_api)
        return self.api_key

    def get_api(self):
        return self.api_key

    # classmethod of Account called api_authenticate
    @classmethod
    def api_authenticate(cls, api_key):
        return cls.one_from_where_clause("WHERE api_key=?",
                                        (api_key,))

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        if self.balance < amount:
            raise ValueError("amount must not be greater than balance")
        self.balance -= amount
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        self.balance += amount
    