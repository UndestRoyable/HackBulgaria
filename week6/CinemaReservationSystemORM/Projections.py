from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

# A class that maps to a table, inherits from Base
Base = declarative_base()


# Our class will be mapped to a table with name student
# Each field is a Column with the given type and constraints
class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey("movies.id"))
    projection = relationship("Movie", backref="projections")
    rating = Column(Float)


engine = create_engine("sqlite:///ReservationSystem.db")
# will create all tables
Base.metadata.create_all(engine)
