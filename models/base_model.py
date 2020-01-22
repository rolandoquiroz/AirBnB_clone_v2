#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
import models
import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from shlex import split
Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = {}
        my_dict = self.__dict__.copy()
        my_dict.update(__class__=self.__class__.__name__)
        if 'created_at' in my_dict:
            my_dict['created_at'] = my_dict['created_at'].isoformat()
        if 'updated_at' in my_dict:
            my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        if '_sa_instance_state' in my_dict:
            del my_dict["_sa_instance_state"]
        return my_dict

    def delete(self):
        """  to delete the current instance from the storage (models.storage).
        by calling the method delete
        """
        models.storage.delete(self)
