import sqlite3
import hashlib
import os

class Database(object):
    def __init__(self):
        self.path = "app/storage/"

        if not os.path.exists(os.path.join(self.path, 'db.sqlite')):
            conn = self.db_connect()
            cur = conn.cursor()

            sql = '''
            CREATE TABLE tasks(id integer primary key, name text not null, 
            date text not null)
            '''

            sql1 = """
            CREATE TABLE users(id integer primary key, name text not null,
            password text not null)
            """

            cur.execute(sql)
            cur.execute(sql1)
    
    def db_connect(self):
        conn = sqlite3.connect(os.path.join(self.path, 'db.sqlite'))
        return conn

    def add_user(self, user: tuple):
        """
        Description of Add user to Database

        Args:
            self (undefined):
            user (tuple):

        """
        conn = self.db_connect()
        cur = conn.cursor()
        
        name, passw = user
        try:
            pwd = hashlib.sha256(passw.encode()).hexdigest()
            userx = (name,pwd)

            sql = "INSERT INTO users(name, password) VALUES(?,?)"
            cur.execute(sql, userx)
            conn.commit()
            return True
        
        except Exception as e:
            print(e)
            return False
        