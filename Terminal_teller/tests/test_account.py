from unittest import TestCase
from app import Account, ORM

import os

from data import schema, seed

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR, DBFILENAME)

ORM.dbpath = DBPATH

class TestAccount(TestCase):
    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        os.remove(DBPATH)

    def testNewAccount(self):
        account1 = Account()
        self.assertEqual(account1.tablename, "accounts")
        self.assertIsInstance(account1, Account)
        self.assertEqual(account1.fields, ["username", "pin", "balance", "api_key"])

        account2 = Account(username="Akil", pin="4456", balance="1200.00")
        api = account2.generate_api_key()
        account2.save()
        get_api = account2.get_api()
        self.assertEqual(api, get_api)
    
    def testLogin(self):
        account3 = Account(username="mike_bloom", pin="1234", balance=20.00)
        api = account3.generate_api_key()
        account3.save()
        get_api = account3.get_api()

        account4 = Account.api_authenticate(get_api)

        self.assertEqual(account4.username, "mike_bloom")
        self.assertEqual(account4.pin, "1234")
        self.assertEqual(account4.balance, 20.00)





