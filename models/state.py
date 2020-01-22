#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="stat", cascade="all,delete")
    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id"""
            all_cities = models.storage.all(City).values()
            return [c for c in all_cities if c.state_id == self.id]
