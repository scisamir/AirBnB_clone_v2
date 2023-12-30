#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity

place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE=db') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')

    else:
        @property
        def reviews(self):
            """ Returns the list of Review instances
            with place_id equals to the current """
            from models import storage
            rev_res = []
            all_reviews = storage.all(Review).values()
            for rev in all_reviews:
                if self.id == rev.place_id:
                    rev_res.append(rev)
            return rev_res

        @property
        def amenities(self):
            """ Returns the list of Amenity instances based
            on the attribute amenity_ids """
            from models import storage
            amts = []
            all_amenities = storage.all(Amenity).values()
            for am in all_amenities:
                if am.id in self.amentity_ids:
                    amts.append(am)
            return amts

        @amenities.setter
        def amenities(self, cls=None):
            """ Handles append method for adding an Amenity.id
            to the attribute amenity_ids """
            if isinstance(cls, Amenity):
                if cls.id not in self.amenity_ids:
                    amneity_ids.append(cls.id)
