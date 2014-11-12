import sqlite3

db = sqlite3.connect('ReservationSystem')
cursor = db.cursor()
#create tables

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, name TEXT,
                       rating REAL);
''')
db.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT,
        date TEXT, time TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id));
    ''')
db.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations(id INTEGER PRIMARY KEY, username INTEGER, projection_id INTEGER,
    row INTEGER, col INTEGER, FOREIGN KEY(projection_id) REFERENCES projections(id));
    ''')
db.commit()

#insert data:
#movies
cursor.execute('''INSERT INTO movies(name, rating)
                  VALUES(?, ?)''', ("The Hunger Games: Catching Fire", 7.9))
print('New movie inserted')

cursor.execute('''INSERT INTO movies(name, rating)
                  VALUES(?, ?)''', ("Wreck-It Ralph", 7.8))
print('New movie inserted')

cursor.execute('''INSERT INTO movies(name, rating)
                  VALUES(?, ?)''', ("Her", 8.3))
print('New movie inserted')

db.commit()
#projections
cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?, ?, ?, ?)''', (1, "3D", "2014-04-01", "19:10"))
print('New projection inserted')

cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?, ?, ?, ?)''', (1, "2D", "2014-04-01", "19:00"))
print('New projection inserted')

cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?, ?, ?, ?)''', (1, "4DX", "2014-04-02", "21:00"))
print('New projection inserted')

cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?, ?, ?, ?)''', (3, "2D", "2014-04-05", "20:20"))
print('New projection inserted')

cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?, ?, ?, ?)''', (2, "3D", "2014-04-02", "22:00"))
print('New projection inserted')

cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?, ?, ?, ?)''', (2, "2D", "2014-04-02", "19:30"))
print('New projection inserted')

db.commit()

#reservations

cursor.execute('''INSERT INTO reservations(username, projection_id , row, col)
                  VALUES(?, ?, ?, ?)''', ("RadoRado", 1, 2, 1))
print('New reservation inserted')

cursor.execute('''INSERT INTO reservations(username, projection_id , row, col)
                  VALUES(?, ?, ?, ?)''', ("RadoRado", 1, 3, 5))
print('New reservation inserted')

cursor.execute('''INSERT INTO reservations(username, projection_id , row, col)
                  VALUES(?, ?, ?, ?)''', ("RadoRado", 1, 7, 8))
print('New reservation inserted')

cursor.execute('''INSERT INTO reservations(username, projection_id , row, col)
                  VALUES(?, ?, ?, ?)''', ("Ivo", 3, 1, 1))
print('New reservation inserted')

cursor.execute('''INSERT INTO reservations(username, projection_id , row, col)
                  VALUES(?, ?, ?, ?)''', ("Ivo", 3, 1, 2))
print('New reservation inserted')

cursor.execute('''INSERT INTO reservations(username, projection_id , row, col)
                  VALUES(?, ?, ?, ?)''', ("Mysterious", 5, 2, 3))
print('New reservation inserted')

cursor.execute('''INSERT INTO reservations(username, projection_id , row, col)
                  VALUES(?, ?, ?, ?)''', ("Mysterious", 5, 2, 4))
print('New reservation inserted')

db.commit()

db.close()
