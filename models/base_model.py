#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    ""BaseModel""
    
    def __init__(self, *args, **kwargs):
        ""Constructor""

        if kwargs:
            for key,value in kwargs.items():
                pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
