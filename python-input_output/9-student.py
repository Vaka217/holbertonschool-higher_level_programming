#!/usr/bin/python3
""" 9-student module"""


class Student:
    """ Class Student that defines a student by name, last name and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""
        return self.__dict__
