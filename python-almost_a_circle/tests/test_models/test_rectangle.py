#!/usr/bin/python3
""" unitest rectangle module"""
import unittest
from models.rectangle import Rectangle
import io
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """ class for test cases related with the Rectangle class"""
    def test_width_and_height(self):
        """ Test Rectangle with width and height"""
        r1 = Rectangle(5, 3)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 3)

    def test_width_height_x(self):
        """ Test Rectangle with width, height and x"""
        r1 = Rectangle(5, 3, 2)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)

    def test_width_height_x_y(self):
        """ Test Rectangle with width, height, x and y"""
        r1 = Rectangle(5, 3, 2, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

    def test_width_type(self):
        """ Test Rectangle with width of different type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("5", 3)

    def test_height_type(self):
        """ Test Rectangle with height of different type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, "3")

    def test_x_type(self):
        """ Test Rectangle with x of different type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 3, "2")

    def test_y_type(self):
        """ Test Rectangle with y of different type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 3, 2, "1")

    def test_id(self):
        """ Test Rectangle with a given ID"""
        r1 = Rectangle(5, 3, 2, 1, 12)
        self.assertEqual(r1.id, 12)

    def test_negative_width(self):
        """ Test Rectangle with width as a negative value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-5, 3)

    def test_negative_height(self):
        """ Test Rectangle with height as a negative value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(5, -3)

    def test_zero_width(self):
        """ Test Rectangle with width as zero"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 3)

    def test_zero_height(self):
        """ Test Rectangle with height as zero"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 0)
    
    def test_negative_x(self):
        """ Test Rectangle with x as negative value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 3, -2)

    def test_negative_y(self):
        """ Test Rectangle with y as negative value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 3, 2, -1)

    def test_area(self):
        """ Test Rectangle if area exists"""
        a1 = Rectangle(5, 3).area()
        self.assertEqual(a1, 15)

    def test_str(self):
        """ Test Rectangle if __str__ exists"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            print(Rectangle(1, 1, 1, 1, 1))
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (1) 1/1 - 1/1\n')

    def test_display_none(self):
        """ Test Rectangle if x and y don't exist"""
        with self.assertRaises(TypeError):
            d1 = Rectangle().display()

    def test_display_one(self):
        """ Test Rectangle if y doesn't exist"""
        with self.assertRaises(TypeError):
            d1 = Rectangle(1).display()

    def test_display(self):
        """ Test Rectangle if display exists"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            Rectangle(5, 3).display()
            assert io_stdout.getvalue() == "#####\n#####\n#####\n"
