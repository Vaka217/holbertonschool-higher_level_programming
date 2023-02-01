#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMethods(unittest.TestCase):
    """ Test methods for max_integer"""
    def test_normal(self):
        """ Normal case"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty(self):
        """ Empty list case"""
        self.assertEqual(max_integer([]), None)

    def test_nointeger(self):
        """ Element not integer case"""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 4])


if __name__ == '__main__':
    unittest.main()
