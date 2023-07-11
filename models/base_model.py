#!/usr/bin/python3
"""Base model."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Class BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize values."""
        if kwargs:
            for i in kwargs:
                if i == 'created_at' or 'updated_at':
                    self.created_at = datetime.strptime(kwargs[i],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Str representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update date to the update_at."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary contain all keys-values."""
        dict_aux = self.__dict__.copy()
        dict_aux['__class__'] = self.__class__.__name__
        dict_aux['created_at'] = self.created_at.isoformat()
        dict_aux['updated_at'] = self.updated_at.isoformat()
        return dict_aux
