#!/usr/bin/python3
#generate a unique identifier for enyone class
import uuid
from datetime import datetime

class BaseModel():
    """BaseModel"""
    
    def __init__(self):
        """Constructor"""
        #generate a identifier unique and convert in the string
        self.id = str(uuid.uuid4())
        #get the date using datatime.now
        self.created_at = datetime.now()
        #update the date
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()

    # return a dictionary with all the values of the instance
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict[' __class__ '] = self.__class__.__name__
        obj_dict[' create_at '] = self.create_at.isoformat()
        obj_dict[' update_at '] = self.update_at.isoformat()
        return obj_dict
