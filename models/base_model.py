#!/usr/bin/python3
"""Base model"""
import uuid
from datetime import datetime


class BaseModel():
    """class BaseModel"""

    def __init__(self):
        """Constructor"""
        # generate a identifier unique and convert in the string
        self.id = str(uuid.uuid4())
        # get the date using datatime.now
        self.created_at = datetime.now()
        # update the date
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    # return a dictionary with all the values of the instance
    def to_dict(self):
        dict_aux = self.__dict__.copy()
        dict_aux['__class__'] = self.__class__.__name__
        dict_aux['created_at'] = self.created_at.isoformat()
        dict_aux['updated_at'] = self.updated_at.isoformat()
        return dict_aux
