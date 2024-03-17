#!/usr/bin/python3
"""Moduls that define the state Class representing a state in Mysql database"""

from sqlalchemy import column, integer, string
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Representing a state for Mysql database
    __taablename__(str): the name of the Mysql table to store states.
    id(sqlalchemy.integer): the state id.
    name(sqlalchemy.string): the state name.
    """

    __tablename__ = "states"
    id = column(integer, primary_key=True)
    name = column(string(128), nullable=False)
