#!/usr/bin/python3
""" unitest rectangle module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import json
import os
import sys
from unittest.mock import patch
from contextlib import redirect_stdout

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

    def test_basic_display(self):
            """Test display without x and y"""
            r = Rectangle(2, 3, 0, 0, 1)
            with io.StringIO() as buf, redirect_stdout(buf):
                r.display()
                output = buf.getvalue()
                self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_display_one(self):
        """ Test Rectangle if y doesn't exist"""
        with self.assertRaises(TypeError):
            d1 = Rectangle(1).display()

    def test_display(self):
        """ Test Rectangle if display exists"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            Rectangle(5, 3).display()
            self.assertEqual(io_stdout.getvalue(), "#####\n#####\n#####\n")

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)

    def test_to_dictionary(self):
        """ Test Rectangle to_dictionary method"""
        r1 = Rectangle(5, 3, 2, 1, 12).to_dictionary()
        self.assertEqual(r1, {'x': 2, 'y': 1, 'id': 12, 'height': 3, 'width': 5})

    def test_update(self):
        """ Test Rectangle update method"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update()
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (12) 2/1 - 5/3\n')

    def test_update_one(self):
        """ Test Rectangle update method with one argument"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(89)
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 2/1 - 5/3\n')

    def test_update_two(self):
        """ Test Rectangle update method with two arguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(89, 2)
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 2/1 - 2/3\n')

    def test_update_three(self):
        """ Test Rectangle update method with three arguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(89, 2, 4)
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 2/1 - 2/4\n')

    def test_update_four(self):
        """ Test Rectangle update method with four arguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(89, 2, 4, 5)
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 5/1 - 2/4\n')

    def test_update_five(self):
        """ Test Rectangle update method with five arguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(89, 2, 4, 5, 7)
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 5/7 - 2/4\n')

    def test_update_kw(self):
        """ Test Rectangle update method with one kwargument"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(**{ 'id': 89 })
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 2/1 - 5/3\n')

    def test_update_kwtwo(self):
        """ Test Rectangle update method with two kwarguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(**{ 'id': 89, 'width': 1 })
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 2/1 - 1/3\n')

    def test_update_kwthree(self):
        """ Test Rectangle update method with three kwarguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(**{ 'id': 89, 'width': 1, 'height': 2 })
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 2/1 - 1/2\n')

    def test_update_kwfour(self):
        """ Test Rectangle update method with four kwarguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 3/1 - 1/2\n')

    def test_update_kwfive(self):
        """ Test Rectangle update method with five kwarguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            r1 = Rectangle(5, 3, 2, 1, 12)
            r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
            print(r1)
            self.assertEqual(io_stdout.getvalue(), '[Rectangle] (89) 3/4 - 1/2\n')

    def test_create_one(self):
        """ Test Rectangle create method with one argument"""
        with io.StringIO() as io_stdout:
            r1 = Rectangle(3, 5, 1).to_dictionary()
            output1 = io_stdout.getvalue()
        with io.StringIO() as io_stdout:
            r2 = Rectangle.create(**r1)
            output2 = io_stdout.getvalue()
        self.assertEqual(output1, output2)

    def save_file_rectangle(self):
        """Test save_to_file() method of Rectangle
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(7, 9)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", mode='r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[{"y": 6, '
                                        '"x": 4, '
                                        '"id": 1, '
                                        '"width": 10, '
                                        '"height": 5}, '
                                        '{"y": 0, '
                                        '"x": 0, '
                                        '"id": 2, '
                                        '"width": 7, '
                                        '"height": 9}]'))
        os.remove("Rectangle.json")

    def save_file_rectangle_none(self):
        """Test save_to_file(None) method of Rectangle
        """
        Base._Base__nb_objects = 0
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", mode='r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[]'))
        os.remove("Rectangle.json")

    def save_file_rectangle_empty(self):
        """Test save_to_file([]) method of Rectangle
        """
        Base._Base__nb_objects = 0
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", mode='r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[]'))
        os.remove("Rectangle.json")

    def load_from_file_no_file(self):
        """Test load_from_file with no file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

