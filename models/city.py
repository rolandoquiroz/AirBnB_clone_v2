#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    states = relationship("State")
