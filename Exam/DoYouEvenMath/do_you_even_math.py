from questions import Question
from players import Player
from highscores import Highscore
from connection import *
import random


class Math:
    def __init__(self):
        Base.metadata.create_all(engine)

    def printWelcomeText(self):
        print("Welcome to Do You Even Math - HackBulgaria edition")
        print("The game rules are simple: The game will answer you")
        print("a question, and your task is to give a correct answer!")
        print("Now you have 2 options:")
        print("-start ---> to start the game")
        print("-highscores ---> to see the Top10 highscores")

    def addQuestions(self, questions, answers):
        session.add(Question(question=questions, answer=answers))
        session.commit()

    def getPlayerName(self):
        player = input("Enter your nickname> ")
        session.add(Player(name=player))
        session.commit()
        print("Player added succesfully to the DB")

    def askQuestion(self):
        random_id = random.randint(1, 10)
        question_to_ask = session.query(Question).filter(Question.id == random_id)
        print(question_to_ask.question)


def main():

    math = Math()
    #math.addQuestions("What is the answer to 1+1", 2)
    #math.addQuestions("What is the answer to square root (sqrt) of 169?", 13)
    #math.addQuestions("What is the answer to (5*5) - (5*2)", 15)
    #math.addQuestions("What is the answer to 2048/1024", 2)
    #math.addQuestions("What is the answer to 2^10", 1024)
    #math.addQuestions("What is the answer to 2^3 + 2", 10)
    #math.addQuestions("What is the answer to -9*-5", 45)
    #math.addQuestions("What is the answer to log(10)", 1)
    #math.addQuestions("What is the answer to x - 69 = 0", 69)

    math.getPlayerName()
    math.askQuestion()

if __name__ == '__main__':
    main()
