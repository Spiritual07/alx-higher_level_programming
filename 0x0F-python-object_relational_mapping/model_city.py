#!/usr/bin/python3

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class representing Cities"""

    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
