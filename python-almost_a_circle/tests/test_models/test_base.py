#!/usr/bin/python3
""" unitest base module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ class for test cases related with the Base class"""
    def test_noargs(self):
        """ Test of Base for assigning automatically an ID"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """ Test of Base for assigning automatically an ID + 1"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1, b3.id - 2)

    def test_save_id(self):
        """ Test of Base for saving an ID"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_to_json_none(self):
        """ Test of Base.to_json_string(None) exists"""
        j1 = Base.to_json_string(None)
        self.assertEqual(j1, '[]')

    def test_to_json_empty(self):
        """ Test of Base.to_json_string([]) exists"""
        j1 = Base.to_json_string([])
        self.assertEqual(j1, '[]')

    def test_to_json(self):
        """ Test of Base.to_json_string({'width': 3})"""
        j1 = Base.to_json_string({'width': 3})
        self.assertEqual(j1, '{"width": 3}')

    def test_to_json_type(self):
        """ Test of Base.to_json_string() returns a string"""
        j1 = Base.to_json_string({'width': 3})
        self.assertIsInstance(j1, str)

    def test_from_json_none(self):
        """ Test of Base.from_json_string(None) exists"""
        j1 = Base.from_json_string(None)
        self.assertEqual(j1, [])

    def test_from_json_empty(self):
        """ Test of Base.from_json_string("[]") exists"""
        j1 = Base.from_json_string("[]")
        self.assertEqual(j1, [])

    def test_from_json(self):
        """ Test of Base.from_json_string('[{"width": 3}]')"""
        j1 = Base.from_json_string('[{"width": 3}]')
        self.assertEqual(j1, [{'width': 3}])

    def test_from_json_type(self):
        """ Test of Base.from_json_string('[{"width": 3}]') type"""
        j1 = Base.from_json_string('[{"width": 3}]')
        self.assertIsInstance(j1, list)
