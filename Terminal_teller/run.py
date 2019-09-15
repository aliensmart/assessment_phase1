from app import controller
from app import ORM
import os


DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'tteller.db')
ORM.dbpath = DBPATH
# Account.dbpath = DBPATH
controller.run()