#!/usr/bin/python3
"""
    Define 'BaseModel' class
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
        Represent 'BaseModel' class
    """

    def __init__(self, *args, **kwargs):
        """
            Initialize new 'BaseModel' instance
            Arguments:
                *args (any): this will not be used.
                **kwargs (dict): this will be used to get keyword arguments passed.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
            Save the model instance to the storage engine
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Return dictionary representation of the model instance
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """
            Return string representation of the model instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
