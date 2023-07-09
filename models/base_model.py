#!/usr/bin/python3
"""Base model"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialize values"""
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'update_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            # generated a identifier unique and convert in the string
            self.id = str(uuid4())
            # get the date using datatime.now
            self.created_at = datetime.now()
            # update the date
            self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update date to the update_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary contain all keys/values"""
        dict_aux = self.__dict__.copy()
        dict_aux['__class__'] = self.__class__.__name__
        dict_aux['created_at'] = self.created_at.isoformat()
        dict_aux['updated_at'] = self.updated_at.isoformat()
        return dict_aux
