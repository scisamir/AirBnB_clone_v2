#!/usr/bin/python3
"""
DBStorage Engine Module
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'User': User, 'Place': Place, 'State': State,
    'City': City, 'Amenity': Amenity, 'Review': Review
}


class DBStorage:
    """ Class DBStorage """

    __engine = None
    __session = None

    def __init__(self):
        """ Init public instance method """
        ms_usr = getenv('HBNB_MYSQL_USER')
        ms_pwd = getenv('HBNB_MYSQL_PWD')
        ms_host = getenv('HBNB_MYSQL_HOST')
        ms_db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
                        'mysql+mysqldb://{}:{}@{}/{}'
                        .format(ms_usr, ms_pwd, ms_host, ms_db),
                        pool_pre_ping=True
                )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """ Query on the database session """
        my_models = {}

        if cls is None:
            for a_class in classes.values():
                a_model = self.__session.query(a_class).all()

                for model in a_model:
                    key = model.__class__.__name__ + '.' + model.id
                    my_models[key] = model

        else:
            a_model = self.__session.query(cls).all()
            for model in a_model:
                key = model.__class__.__name__ + '.' + model.id
                my_models[key] = model

        return my_models

    def new(self, obj):
        """ Adds 'obj' object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        Session = scoped_session(session_factory)
        self.__session = Session()
