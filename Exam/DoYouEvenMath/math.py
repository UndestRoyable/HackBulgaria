from create_database import savePlayer

def printWelcomeText():
    print("Welcome to Do You Even Math - HackBulgaria edition")
    print("The game rules are simple: The game will answer you")
    print("a question, and your task is to give a correct answer!")
    print("Now you have 2 options:")
    print("-start ---> to start the game")
    print("-highscores ---> to see the Top10 highscores")


def getPlayerName():
    player_name = input("Enter your playername>")
    savePlayer(player_name)

getPlayerName()
