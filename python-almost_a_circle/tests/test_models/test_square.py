#!/usr/bin/python3
""" unitest square module"""
import unittest
from models.square import Square
import io
import os
from unittest.mock import patch
from contextlib import redirect_stdout

class TestSquare(unittest.TestCase):
    """ class for test cases related with the Square class"""
    def test_size(self):
        """ Test Square with size"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_x(self):
        """ Test Square with size and x"""
        s1 = Square(5, 3)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 3)

    def test_size_x_y(self):
        """ Test Square with size, x and y"""
        s1 = Square(5, 2, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)

    def test_size_type(self):
        """ Test Square with size of different type"""
        with self.assertRaises(TypeError):
            s1 = Square("5")

    def test_x_type(self):
        """ Test Square with x of different type"""
        with self.assertRaises(TypeError):
            s1 = Square(5, "3")

    def test_y_type(self):
        """ Test Square with y of different type"""
        with self.assertRaises(TypeError):
            s1 = Square(5, 3, "2")

    def test_id(self):
        """ Test Square with a given ID"""
        s1 = Square(5, 3, 2, 12)
        self.assertEqual(s1.id, 12)

    def test_negative_size(self):
        """ Test Square with size as a negative value"""
        with self.assertRaises(ValueError):
            s1 = Square(-5)

    def test_negative_x(self):
        """ Test Square with x as a negative value"""
        with self.assertRaises(ValueError):
            s1 = Square(5, -3)

    def test_negative_y(self):
        """ Test Rectangle with y as a negative value"""
        with self.assertRaises(ValueError):
            s1 = Square(5, 3, -2)
    
    def test_zero_size(self):
        """ Test Square with size as zero"""
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_str(self):
        """ Test Square if __str__ exists"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            print(Square(3, 1, 3, 12))
            self.assertEqual(io_stdout.getvalue(), '[Square] (12) 1/3 - 3\n')

    def test_to_dictionary(self):
        """ Test Square to_dictionary method"""
        s1 = Square(3, 1, 3, 12).to_dictionary()
        self.assertEqual(s1, {'x': 1, 'y': 3, 'id': 12, 'size': 3})

    def test_update(self):
        """ Test Square update method"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update()
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (12) 3/2 - 5\n')

    def test_update_one(self):
        """ Test Square update method with one argument"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update(89)
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (89) 3/2 - 5\n')

    def test_update_two(self):
        """ Test Square update method with two arguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update(89, 4)
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (89) 3/2 - 4\n')

    def test_update_three(self):
        """ Test Square update method with three arguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update(89, 4, 6)
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (89) 6/2 - 4\n')

    def test_update_four(self):
        """ Test Square update method with four arguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update(89, 2, 4, 7)
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (89) 4/7 - 2\n')

    def test_update_kw(self):
        """ Test Square update method with one kwargument"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update(**{ 'id': 89 })
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (89) 3/2 - 5\n')

    def test_update_kwtwo(self):
        """ Test Square update method with two kwarguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update(**{ 'id': 89, 'size': 1 })
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (89) 3/2 - 1\n')

    def test_update_kwthree(self):
        """ Test Square update method with three kwarguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update(**{ 'id': 89, 'size': 1, 'x': 4 })
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (89) 4/2 - 1\n')

    def test_update_kwfour(self):
        """ Test Square update method with four kwarguments"""
        with patch('sys.stdout', new=io.StringIO()) as io_stdout:
            s1 = Square(5, 3, 2, 12)
            s1.update(**{ 'id': 89, 'size': 1, 'x': 4, 'y': 3 })
            print(s1)
            self.assertEqual(io_stdout.getvalue(), '[Square] (89) 4/3 - 1\n')

    def test_create_one(self):
        """ Test Square create method with one argument"""
        with io.StringIO() as io_stdout:
            s1 = Square(3, 5).to_dictionary()
            output1 = io_stdout.getvalue()
        with io.StringIO() as io_stdout:
            s2 = Square.create(**s1)
            output2 = io_stdout.getvalue()
        self.assertEqual(output1, output2)

    def save_to_none(self):
        """ Test Square.save_to_file(None)"""
        Square.save_to_file(None)
        if os.path.exists('Square.json'):
            with open("Square.json", "r") as f:
                print(f.read())
            with patch('sys.stdout', new=io.StringIO()) as io_stdout:
                self.assertEqual(io_stdout.getvalue(), "[]\n")

    def save_to_none(self):
        """ Test Square.save_to_file([])"""
        Square.save_to_file([])
        if os.path.exists('Square.json'):
            with open("Square.json", "r") as f:
                print(f.read())
            with patch('sys.stdout', new=io.StringIO()) as io_stdout:
                self.assertEqual(io_stdout.getvalue(), "[]\n")

    def save_to_file(self):
        """ Test Square.save_to_file() regular cases"""
        s1 = Square(1, 5, 7, 3)
        s2 = Square(1, 1, 1, 1)
        Square.save_to_file([r1, r2])
        if os.path.exists('Square.json'):
            with open("Square.json", "r") as f:
                print(f.read())
            with patch('sys.stdout', new=io.StringIO()) as io_stdout:
                self.assertEqual(io_stdout.getvalue(), '[{"id": 3, "size": 1, \
"x": 5, "y": 7}, {"id": 1, "size": 1, "x": 1, "y": 1}]\n')
    @classmethod
    def tearDown(self):
        """Delete files."""
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def save_to_file_None(self):
        """ Test Square.save_to_file(None)"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def save_to_file_empty_list(self):
        """ Test Square.save_to_file([])"""
        Square.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def save_to_file_square(self):
        """ Test Square.save_to_file() regular cases"""
        r1 = Square(10, 7, 2, 8)
        Square.save_to_file([r1])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_load_from_file_no_file(self):
        """Test load_from_file with no file"""
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])

