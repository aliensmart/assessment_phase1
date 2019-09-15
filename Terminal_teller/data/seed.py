import sqlite3
import os
from app import ORM, Account

DIR = os.path.dirname(__file__)
DBFILENAME = "tteller.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath

    abdoul = Account(username="abdoul", pin="3212", 
    balance=2000.00)
    abdoul.save()
    # abdoul.generate_api_key()
    # abdoul.save()
    # print(abdoul.api_key)

    