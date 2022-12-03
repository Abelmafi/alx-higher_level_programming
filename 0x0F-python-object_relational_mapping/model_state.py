#!/usr/bin/python3
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence


Base = declarative_base()


class State(Base):
    """ class definition of a State"""

    __tablename__ = 'states'
    id = Column(Integer, Sequence('user_id_seq'),
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    fullname = Column(String(50))
