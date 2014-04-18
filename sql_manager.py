import hashlib
import sqlite3
import smtplib
import getpass
import time
import re
from random import random
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def _check_symbols(password):
    special_symbols = r'\W+'
    has_special = bool(re.search(special_symbols, password))
    lowercase = r'[a-z]'
    has_lower = bool(re.search(lowercase, password))
    uppercase = r'[A-Z]'
    has_upper = bool(re.search(uppercase, password))
    numbers = r'[0-9]'
    has_digit = bool(re.search(numbers, password))
    return (has_special, has_lower, has_upper, has_digit)


def _hash(password):
    m = hashlib.sha1()
    m.update(password.encode('utf-8'))
    password = m.hexdigest()
    return password


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                email TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                attempts INTEGER DEFAULT 0,
                failed_attempts_time INTEGER DEFAULT 0,
                hash TEXT,
                hash_time INTEGER DEFAULT 0,
                tans TEXT DEFAULT "0,0,0,0,0,0,0,0,0,0")'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = ("UPDATE clients SET message = ? WHERE id = ?")
    update_sql_data = [new_message, logged_user.get_id()]
    cursor.execute(update_sql, update_sql_data)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    if len(new_pass) < 8:
        print('Password must be at least 8 symbols!')
    elif all(_check_symbols(new_pass)) is False:
        print('Password must contain both lowercase and uppercase letters,')
        print('special symbols and numbers.')
    else:
        new_pass = _hash(new_pass)
        update_sql = ("UPDATE clients SET password = ? WHERE id = ?")
        update_sql_data = [new_pass, logged_user.get_id()]
        cursor.execute(update_sql, update_sql_data)
        conn.commit()


def register(username, password, email):
    if len(password) < 8:
        print('Password must be at least 8 symbols!')
        return False
    elif all(_check_symbols(password)) is False:
        print('Password must contain both lowercase and uppercase letters,')
        print('special_symbols and numbers.')
        return False
    else:
        print("Registration Successfull")
        password = _hash(password)
        insert_sql = ("""INSERT INTO clients (username, password, email)
                         VALUES (?, ?, ?)""")
        insert_sql_data = [username, password, email]
        cursor.execute(insert_sql, insert_sql_data)
        conn.commit()


def login(username, password):
    query = ("SELECT failed_attempts_time FROM clients WHERE username = ?")
    data = [username]
    cursor.execute(query, data)
    block_time = cursor.fetchone()[0]
    if int(time.time()) - 300 > block_time:
        password = _hash(password)
        select_query = ("""SELECT id, username, email, balance,
                                  message, attempts, failed_attempts_time
                           FROM clients
                           WHERE username = ? AND password = ?
                           LIMIT 1""")
        select_data = [username, password]

        cursor.execute(select_query, select_data)
        user = cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3], user[4])
        else:
            query = ("SELECT attempts FROM clients WHERE username = ?")
            data = [username]
            cursor.execute(query, data)
            attempts = cursor.fetchone()[0]
            if attempts + 1 == 5:
                print('Drop the banhammer!')
                query = ('UPDATE clients SET failed_attempts_time = ?')
                data = [int(time.time())]
                cursor.execute(query, data)
                conn.commit()
                attempts = 0
            attempts_query = ("UPDATE clients SET attempts = ?")
            attempts_data = [attempts + 1]
            cursor.execute(attempts_query, attempts_data)
            conn.commit()
            return False
    else:
        print('This user is blocked! Try in a few minutes!')


def send_reset_pass_email(username):
    query = ('SELECT email FROM clients WHERE username = ?')
    data = [username]
    cursor.execute(query, data)
    sender = 'pytestemail@gmail.com'
    address = cursor.fetchone()[0]
    message = hashlib.sha1(str(random()).encode('utf-8')).hexdigest()
    query = ('UPDATE clients SET hash = ?, hash_time = ?')
    data = [message, time.time()]
    cursor.execute(query, data)
    conn.commit()
    name = 'pytestemail'
    password = 'passtest'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(name, password)
    server.sendmail(sender, address, message)
    server.quit()


def reset_password(username, message):
    query = ('SELECT hash, hash_time FROM clients WHERE username = ?')
    data = [username]
    cursor.execute(query, data)
    hash = cursor.fetchone()[0]
    hash_time = cursor.fetchone()[1]
    if time.time() - 900 > hash_time:
        query = ('UPDATE clients SET hash = ? WHERE username = ?')
        data = [0, username]
        cursor.execute(query, data)
        conn.commit()
    if message == hash:
        query = ('UPDATE clients SET hash = ? WHERE username = ?')
        data = [0, username]
        cursor.execute(query, data)
        conn.commit()
        new_pass = getpass.getpass("Enter your password: ")
        if len(new_pass) < 8:
            print('Password must be at least 8 symbols!')
        elif all(_check_symbols(new_pass)) is False:
            print('Password must contain lowercase, uppercase letters,')
            print('special_symbols and numbers.')
        else:
            new_pass = _hash(new_pass)
            query = ('SELECT id FROM clients WHERE username = ?')
            data = [username]
            cursor.execute(query, data)
            id = cursor.fetchone()[0]
            update_sql = ("UPDATE clients SET password = ? WHERE id = ?")
            update_sql_data = [new_pass, id]
            cursor.execute(update_sql, update_sql_data)
            conn.commit()
    else:
        print('Wrong hash code! Try again!')


def deposit(amount, tan, logged_user):
    if tan == '0':
        print('TAN code invalid!')
    else:
        if float(amount) <= 0:
            print('Invalid amount of money, please try again!')
        else:
            query = ('SELECT tans FROM clients WHERE username = ?')
            data = [logged_user.get_username()]
            cursor.execute(query, data)
            tans = cursor.fetchone()[0]
            tans_list = tans.split(',')
            if tan in tans_list:
                tans_list[tans_list.index(tan)] = '0'
                query = ('SELECT balance FROM clients WHERE id = ?')
                data = [logged_user.get_id()]
                cursor.execute(query, data)
                balance = cursor.fetchone()[0]
                balance += float(amount)
                update_query = ('''UPDATE clients SET balance = ?, tans = ?
                                   WHERE id = ?''')
                update_data = [balance, ','.join(tans_list),
                               logged_user.get_id()]
                cursor.execute(update_query, update_data)
                conn.commit()
                print('Transaction successful!')
                print('Deposited ${} into your bank acount!'.format(amount))
            else:
                print('TAN code invalid!')


def withdraw(amount, tan, logged_user):
    if tan == '0':
        print('TAN code invalid')
    else:
        query = ('SELECT balance FROM clients WHERE id = ?')
        data = [logged_user.get_id()]
        cursor.execute(query, data)
        balance = cursor.fetchone()[0]
        if float(amount) > balance:
            print('Insufficient funds! Try again!')
        else:
            query = ('SELECT tans FROM clients WHERE username = ?')
            data = [logged_user.get_username()]
            cursor.execute(query, data)
            tans = cursor.fetchone()[0]
            tans_list = tans.split(',')
            if tan in tans_list:
                tans_list[tans_list.index(tan)] = '0'
                balance -= float(amount)
                update_query = ('''UPDATE clients SET balance = ?, tans = ?
                                   WHERE id = ?''')
                update_data = [balance, ','.join(tans_list),
                               logged_user.get_id()]
                cursor.execute(update_query, update_data)
                conn.commit()
                print('Transaction successful!')
                print('${} withdrawn from your bank acount!'.format(amount))
            else:
                print('TAN code invalid!')


def display_balance(logged_user):
    query = ('SELECT balance FROM clients WHERE id = ?')
    data = [logged_user.get_id()]
    cursor.execute(query, data)
    balance = cursor.fetchone()[0]
    return balance


def get_tan(logged_user):
    query = ('SELECT tans FROM clients WHERE username = ?')
    data = [logged_user.get_username()]
    cursor.execute(query, data)
    tans = cursor.fetchone()[0]
    tans_list = tans.split(',')
    if tans_list == ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']:
        query = ('SELECT email FROM clients WHERE username = ?')
        cursor.execute(query, data)
        sender = 'pytestemail@gmail.com'
        address = cursor.fetchone()[0]
        tan_codes = []
        for i in range(10):
            tan_codes.append(
                hashlib.sha1(str(random()).encode('utf-8')).hexdigest())
        message = '\n'.join(tan_codes)
        query = ('UPDATE clients SET tans = ?')
        data = [message.replace('\n', ',')]
        cursor.execute(query, data)
        conn.commit()
        name = 'pytestemail'
        password = 'passtest'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(name, password)
        server.sendmail(sender, address, message)
        server.quit()
        print('Sent TAN codes to your email!')
        return tan_codes
    else:
        count = 10
        for tan in tans_list:
            if tan == '0':
                count -= 1
        print('You still have {} TANS left!'.format(count))
        return tans_list
