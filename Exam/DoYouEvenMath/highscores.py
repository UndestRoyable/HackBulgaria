from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection import *


class Highscore(Base):
    __tablename__ = "highscore"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    player_id = Column(Integer, ForeignKey("player.id"))
    player = relationship("Player", backref="scores")
