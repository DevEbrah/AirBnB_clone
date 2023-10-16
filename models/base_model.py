#!/usr/bin/python3
"""BaseModel class for Air bnb"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import String, Integer, Column, DateTime

Base = declarative_base()

class BaseModel:
    """This class will define its attributes and classes"""
    id = Column(String(50), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))


    def __init__(self, *args, **kwargs):
        """Defining instance attributes
        Args:
        kwargs: argument for the constructor of the BaseModel
        Attributes
        id: unique id generated
        create_at: creation date
        update_at: update date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        
    def _str_(self):
        """Returns a string
            Return:
            returns a string of class name, id and dictionary"""
        return "[{}] ({}) {}".format( type(self)._name_, self.id, self._dict_)
    def _repr_(self):
        """return a string representation"""
        return self._str_()

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
    my_dict = dict(self.__dict__)
    my_dict["__class__"] = str(type(self).__name__)
    my_dict["created_at"] = self.created_at.isoformat()
    my_dict["updated_at"] = self.updated_at.isoformat()
    if '_sa_instance_state' in my_dict.keys():
        del my_dict['_sa_instance_state']
    return my_dict

def delete(self):
    """ delete object"""
    models.get_storage.delete(self)
