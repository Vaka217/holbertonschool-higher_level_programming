#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMethods(unittest.TestCase):
    """ Test methods for max_integer"""
    def test_max_at_end(self):
        """ Max value at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """ Max value at the beginning"""
        self.assertEqual(max_integer([7, 3, 1]), 7)

    def test_max_at_middle(self):
        """ Max value at the middle"""
        self.assertEqual(max_integer([1, 9, 3]), 9)

    def test_empty(self):
        """ Empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_negative(self):
        """ One negative value in the list"""
        self.assertEqual(max_integer([4, -3, 2]), 4)

    def test_all_negative(self):
        """ All negative values in the list"""
        self.assertEqual(max_integer([-9, -2, -5]), -2)

    def test_one_only(self):
        """ List of one element"""
        self.assertEqual(max_integer([9]), 9)


if __name__ == '__main__':
    unittest.main()
