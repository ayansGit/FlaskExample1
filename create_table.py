import sqlite3
from util import DATABASE_NAME, USER_TABLE

def create_user_table():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    create_table = f"CREATE TABLE IF NOT EXISTS {USER_TABLE} (id INTEGER PRIMARY KEY, username text, password text, fullname text, phone int)"
    cursor.execute(create_table)
    connection.commit()
    connection.close()

