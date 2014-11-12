import sqlite3

db = sqlite3.connect('ReservationSystem')
db.row_factory = sqlite3.Row
cursor = db.cursor()


def print_menu():
    commands = ["show_movies", "show_movie_projections <movie_id> [<date>]", "make_reservation",
                "cancel_reservation", "exit", "help"]
    print("Hello! I'm your magic reservation system!")
    print("You have the following commands:")
    command_id = 0
    for command in commands:
        command_id += 1
        print("[{}]".format(command_id) + command + "\n")


def show_movies():
    result = cursor.execute('''SELECT * FROM movies ORDER BY rating desc;''')
    movie_counter = 0
    for row in result:
        movie_counter += 1
        print("[{}] - {} ({})".format(row["id"], row["name"], row["rating"]))


def show_movie_proejections(movie_id):
    selected_id = movie_id
    result = cursor.execute('''SELECT projections.id, movies.name, projections.type,
    projections.date, projections.time
    FROM projections
    LEFT OUTER JOIN movies ON projections.movie_id = movies.id
    WHERE movie_id = ?''', (selected_id,))
    for row in result:
        print("[{}] - {} {} ({})".format(row["id"], row["date"], row["time"], row["type"]))


def make_reservation():
    
    name = input("Enter your name: ")
    number_of_tickets = input("Enter number of tickets: ")
    show_movies()
    movie_choose = input("Choose a movie: ")
    show_movie_proejections(movie_choose)
    projection_choose = input("Choose a projection: ")

#---------------------------------------------------------------------------------------------

print_menu()

command = input("Enter command: ")
if command == "show_movies":
    show_movies()
elif command == "show_movie_projections":
    movie_id = input("Enter movie ID: ")
    #movie_date = input("Enter date in format YY-MM-DD(optional): ")

    show_movie_proejections(movie_id)
elif command == "make_reservation":
    make_reservation()

