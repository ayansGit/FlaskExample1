import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

#user = (1, "ayan", "12345")
insert_query = "INSERT INTO users VALUES (?,?,?)"
#cursor.execute(insert_query, user)

users = [
    (1, "ayan", "12345"),
    (2, "tito", "12345"),
    (3, "soumya", "12345")
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()