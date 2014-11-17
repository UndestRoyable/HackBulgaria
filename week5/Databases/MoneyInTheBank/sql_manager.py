import requests
import sqlite3
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    cursor.execute('''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)''')


def change_message(new_message, logged_user):
    #update_sql = "UPDATE clients SET message = '%s' WHERE id = '%s'" % (new_message, )
    cursor.execute("UPDATE clients SET message = ? WHERE id = ?", (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    #update_sql = "UPDATE clients SET password = '%s' WHERE id = '%s'" % (new_pass, logged_user.get_id())
    cursor.execute("UPDATE clients SET password = ? WHERE id = ?", (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    insert_sql = "insert into clients (username, password) values ('%s', '%s')" % (username, password)
    cursor.execute(insert_sql)
    conn.commit()


def login(username, password):
    #select_query = "SELECT id, username, balance, message
    #FROM clients WHERE username = '%s' AND password = '%s' LIMIT 1" % (username, password)
    cursor.execute('''SELECT id, username, balance, message
                      FROM clients
                      WHERE username = ? AND password = ? LIMIT 1''', (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
