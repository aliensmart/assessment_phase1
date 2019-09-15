import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "tteller.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as connect:
        cur = connect.cursor()
        SQL = "DROP TABLE IF EXISTS accounts;"

        cur.execute(SQL)

        SQL = """CREATE TABLE accounts(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR,
            pin VARCHAR,
            balance FLOAT,
            api_key VARCHAR(20)
        );
        """

        cur.execute(SQL)