#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state')

    else:
        @property
        def cities(self):
            """ Gets state associated cities """
            from models import storage

            related_cities = []
            all_cities = storage.all(City).values()

            for a_city in all_cities:
                if self.id == a_city.state_id:
                    related_cities.append(a_city)
            return related_cities
