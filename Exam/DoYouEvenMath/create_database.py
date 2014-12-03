from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

Base = declarative_base()


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(Integer)


class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


class Highscore(Base):
    __tablename__ = "highscore"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    player_id = Column(Integer, ForeignKey("player.id"))
    player = relationship("Player", backref="scores")
    

engine = create_engine("sqlite:///math.db")

Base.metadata.create_all(engine)

#  Adding some data to the database
session = Session(bind=engine)

print("Adding new questions to the database")
question1 = Question(question="What is the answer to 1+1", answer=2)
session.add(question1)

question2 = Question(question="What is the answer to square root (sqrt) of 169?", answer=13)
session.add(question2)

question3 = Question(question="What is the answer to (5*5) - (5*2)", answer=15)
session.add(question3)

question4 = Question(question="What is the answer to 2048/1024", answer=2)
session.add(question4)

question5 = Question(question="What is the answer to 1+1", answer=2)
session.add(question5)

question6 = Question(question="What is the answer to 2^10", answer=1024)
session.add(question6)

question7 = Question(question="What is the answer to 2^3 + 2", answer=10)
session.add(question7)

question8 = Question(question="What is the answer to -9*-5", answer=45)
session.add(question8)

question9 = Question(question="What is the answer to log(10)", answer=1)
session.add(question9)

question10 = Question(question="What is the answer to x - 69 = 0", answer=69)
session.add(question10)

session.commit()


def savePlayer(player_name):
    session = Session(bind=engine)
    player = Player(name=player_name)
    session.add(player)
    session.commit
