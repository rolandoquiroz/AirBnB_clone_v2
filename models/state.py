#!/usr/bin/python3
"""This is the state class"""
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
    cityes = relationship("City", backref="stat", cascade="all,delete")

    @property
    def city(self):
        """returns the list of City instances with state_id"""
        all_cities = storage.all(City)
        cities_list = []
        for city in all_cities.values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list

    if (getenv('HBNB_TYPE_STORAGE') != "db"):
        @property
        def cities(self):
            """returns list of city
            instances with
            matching state_id
            """
            cityObjs = models.storage.all('City').values()
            return [c for c in cityObjs if c.state_id == self.id]
