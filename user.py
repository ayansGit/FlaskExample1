import sqlite3
from util import DATABASE_NAME, USER_TABLE

class User:
    def __init__(self, _id, username, password, fullname, phone):
        self.id = _id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.phone = phone

    @classmethod
    def find_by_username(cls, username):
        connection  = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        query = f"SELECT * FROM {USER_TABLE} WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        #print(row)
        #u = cls(row[0], row[1], row[2])
        if row:
             u = cls(*row)  # or we can do like this user = self(*row)
        else: 
            u = None
        
        connection.close()
        if u:
            return u.__dict__
        else: None

    @classmethod
    def check_if_user_exist(cls, username, phone):
        connection  = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        query = f"SELECT * FROM {USER_TABLE} WHERE username=? OR phone=?"
        result = cursor.execute(query, (username, phone,))
        row = result.fetchone()
        #print(row)
        #u = cls(row[0], row[1], row[2])
        if row:
             u = cls(*row)  # or we can do like this user = self(*row)
        else: 
            u = None
        
        connection.close()
        if u:
            return u.__dict__
        else: None


    @classmethod
    def find_by_id(self, _id):
        connection  = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        query = f"SELECT * FROM {USER_TABLE} WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
             u = self(*row) 
        else: 
            u = None
        connection.close()
        if u:
            return u.__dict__
        else: None

    @classmethod
    def register(self, fullname, phone, username, password):
        connection  = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        insert_query = f"INSERT INTO {USER_TABLE} VALUES (NULL,?,?,?,?)"
        user = (username, password, fullname, phone)
        cursor.execute(insert_query, user)
        connection.commit()
        connection.close()
        
