import sqlite3

db = sqlite3.connect('company')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT,
                       monthly_salary INTEGER, yearly_bonus INTEGER , position TEXT)
''')

cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                  VALUES(?, ?, ?, ?)''', ("Ivan Ivanov", 5000, 10000, "Software Developer"))
print('First user inserted')

cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                  VALUES(?, ?, ?, ?)''', ("RadoRado", 500, 0, "Technical Support Intern"))
print('Second user inserted')

cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                  VALUES(?, ?, ?, ?)''', ("Ivo Ivo", 10000, 10000, "CEO"))
print('Third user inserted')

cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                  VALUES(?, ?, ?, ?)''', ("Petar Petrov", 3000, 1000, "Marketing Manager"))
print('Fourth user inserted')

cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                  VALUES(?, ?, ?, ?)''', ("Maria Georgieva", 8000, 10000, "COO"))
print('Fifth user inserted')

db.commit()

db.close()
