#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage_type

if storage_type == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if storage_type == 'db':
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime(timezone=True),
                            nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime(timezone=True),
                            nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key in kwargs.keys():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = kwargs[key]

            """ time_now = datetime.strptime(datetime.now(),
                                         "%Y-%m-%dT%H:%M:%S.%f") """
            self.created_at = kwargs.get('created_at', datetime.now())
            self.updated_at = kwargs.get('updated_at', datetime.now())
            self.id = kwargs.get('id', str(uuid.uuid4()))

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # delete key -> _sa_instance_state only if it exists
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        storage.delete(self)
