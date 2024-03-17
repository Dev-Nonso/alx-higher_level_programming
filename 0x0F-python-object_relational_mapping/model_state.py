#!/usr/bin/python3
"""Module that defines the State class representing a state in MySQL database"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """Representing a state for MySQL database
    
    __tablename__ (str): the name of the MySQL table to store states.
    id (sqlalchemy.Integer): the state id.
    name (sqlalchemy.String): the state name.
    """

    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
