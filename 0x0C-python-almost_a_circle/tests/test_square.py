#!/usr/bin/python3
"""Unitest module for Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testing...."""

    def test_square_attr(self):
        s1 = Square(5)
        expected_output = "[Square] (14) 0/0 - 5\n"
        with patch('sys.stdout', new = StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_area(self):
        s1 = Square(6)
        self.assertEqual(s1.area(), 36)

    def test_square_disp(self):
        s1 = Square(3)
        expected_output = "###\n###\n###\n"
        with patch('sys.stdout', new = StringIO()) as out:
            s1.display()
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_disp_2(self):
        s2 = Square(3, 1, 3)
        expected_output = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new = StringIO()) as out:
            s2.display()
            self.assertEqual(out.getvalue(), expected_output)

    def test_raise_square_str_size(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.size = '10'

    def test_raise_square_str_x(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.x = '10'
    
    def test_raise_square_str_y(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.y = '10'
    
    def test_raise_square_set_size(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.size = {}
    
    def test_raise_square_set_x(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.x = {1}
    
    def test_raise_square_set_y(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.y = {2}
    
    def test_raise_square_list_size(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.size = [2]
    
    def test_raise_square_list_x(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.x = [2]
    
    def test_raise_square_list_y(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r2.y = [2]
    
    def test_raise_square_value_size(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r2.size = -2
    
    def test_raise_square_value_x(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r2.x = -2
    def test_raise_square_value_y(self):
        r2 = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r2.y = -2

    def test_square_update_1(self):
        s1 = Square(5)
        s1.update(10)
        expected_output = "[Square] (10) 0/0 - 5\n"
        with patch('sys.stdout', new = StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_update_2(self):
        s1 = Square(5)
        s1.update(1, 2)
        expected_output = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new = StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_update_3(self):
        s1 = Square(5)
        s1.update(1, 2, 3)
        expected_output = "[Square] (1) 3/0 - 2\n"
        with patch('sys.stdout', new = StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_update_4(self):
        s1 = Square(5)
        s1.update(5, 2, 3, 4)
        expected_output = "[Square] (5) 3/4 - 2\n"
        with patch('sys.stdout', new = StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_update_5(self):
        s1 = Square(5)
        s1.update(size=7, id=89, y=1)
        expected_output = "[Square] (89) 0/1 - 7\n"
        with patch('sys.stdout', new = StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_to_dict_1(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(s1_dictionary, {'id': 17, 'x': 2, 'size': 10, 'y': 1})

    def test_square_to_dict_2(self):
        s1 = Square(10)
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(s1_dictionary, {'id': 18, 'x': 0, 'size': 10, 'y': 0})
        


 




