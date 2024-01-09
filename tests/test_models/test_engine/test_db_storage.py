#!/usr/bin/python3
"""
Unit Tests for DB Storage
"""
import unittest
import MySQLdb
from os import getenv
from models import storage
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from console import HBNBCommand


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
    "This test is only supported for db storage")
class TestDBStorage(unittest.TestCase):
    """ Test Class for DBStorage """

    @classmethod
    def SetUpClass(cls):
        """ Set up class """
        cls.dbstorage = DBStorage()

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        del cls.dbstorage

    def test_db_new(self):
        """ Test new """
        new_usr = User(email='exp@mail.com', password='exp')
        self.assertEqual(new_usr.email, 'exp@mail.com')

    def test_db_new_and_save(self):
        """ Test new and save """
        new_st = State(name='Lagos')
        storage.new(new_st)
        res = storage.all('State')
        my_list = []
        for key in res.keys():
            my_list.append(key.split('.')[1])
        self.assertTrue(new_st.id in my_list)

    def test_db_all(self):
        """ Test all and console """
        storage.reload()
        res = storage.all()
        self.assertIsInstance(res, dict)

        console = HBNBCommand()
        console.onecmd("create State name=Lagos")
        res = storage.all('State')
        self.assertTrue(len(res) > 0)

    def test_db_delete(self):
        """ Test delete """
        new_st = State(name='Lagos')
        new_st_key = f"State.{new_st.id}"
        storage.new(new_st)
        storage.save()
        old_states = storage.all('State')
        storage.delete(old_states[new_st_key])
        new_states = storage.all('State')
        self.assertNotEqual(len(old_states), len(new_states))
