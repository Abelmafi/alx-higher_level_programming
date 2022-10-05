#!/usr/bin/python3
"""Unitest module for Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare_instantation(unittest.TestCase):
    """Unitest squire method"""

    def test_is_Base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_Square(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(1, 2, 3, 4).size)

    def test_x_setter(self):
        s = Square(1, 2, 3, 4)
        s.x = 10
        self.assertEqual(10, s.x)
    
    def test_x_getter(self):
        self.assertEqual(2, Square(1, 2, 3, 4).x)

    def test_y_setter(self):
        s = Square(1, 2, 3, 4)
        s.y = 10
        self.assertEqual(10, s.y)

    def test_y_getter(self):
        self.assertEqual(3, Square(1, 2, 3, 4).y)

    def test_square_one_Arg(self):
        s = Square(5)
        expected_output = "[Square] ({}) 0/0 - 5\n".format(s.id)
        with patch('sys.stdout', new = StringIO()) as out:
            print(s)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_two_Arg(self):
        s = Square(5, 6)
        expected_output = "[Square] ({}) 6/0 - 5\n".format(s.id)
        with patch('sys.stdout', new = StringIO()) as out:
            print(s)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_three_Arg(self):
        s = Square(5, 6, 7)
        expected_output = "[Square] ({}) 6/7 - 5\n".format(s.id)
        with patch('sys.stdout', new = StringIO()) as out:
            print(s)
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_singleArg(self):
        s = Square(5, 6, 7, 8)
        expected_output = "[Square] ({}) 6/7 - 5\n".format(s.id)
        with patch('sys.stdout', new = StringIO()) as out:
            print(s)
            self.assertEqual(out.getvalue(), expected_output)

    def test_size_setter(self):
        s = Square(2, 2, 2, 2)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_size_getter(self):
        s = Square(2, 2, 2, 2)
        self.assertEqual(s.size, 2)


class TestSquare_instantation_order(unittest.TestCase):
    """Unittest test order of intantation."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2", "3")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2", 2, "8")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "3", "3")


class TestSquare_update(unittest.TestCase):
    """Unittest Square update."""

    def test_update_zero_args(self):
        s = Square(2, 2, 2, 2)
        s.update()
        self.assertEqual("[Square] (2) 2/2 - 2", str(s))

    def test_update_size_args(self):
        s = Square(2, 2, 2, 2)
        s.update(89, 3)
        expected_output = "[Square] ({}) 2/2 - 3\n".format(s.id)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_all_args(self):
        s = Square(2, 2, 2, 2)
        s.update(89, 4, 5, 6)
        expected_output = "[Square] (89) 5/6 - 4\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_all_args_twice(self):
        s = Square(2, 2, 2, 2)
        s.update(89, 3, 5, 6)
        s.update(33, 8, 8, 8)
        expected_output = "[Square] (33) 8/8 - 8\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_args_size_type(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(2, "invalid")

    def test_update_args_size_zero(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(2, 0)

    def test_update_args_size_negetive(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(1, -2)

    def test_update_args_x_type(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(2, 3, "invalid")

    def test_update_args_x_negative(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(89, 2, -1)

    def test_update_args_y_type(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 3, 3, "invalid")

    def test_update_args_y_negative(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(89, 2, 2, -2)


class TestSquare_kwarg_update(unittest.TestCase):
    """Unittest for kwarg input"""

    def test_update_zero_kwargs(self):
        s = Square(2, 2, 2, 2)
        s.update()
        self.assertEqual("[Square] (2) 2/2 - 2", str(s))

    def test_update_size_kwargs(self):
        s = Square(2, 2, 2, 2)
        s.update(size=9)
        expected_output = "[Square] ({}) 2/2 - 9\n".format(s.id)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_all_kwargs(self):
        s = Square(2, 2, 2, 2)
        s.update(size=4, id=89, x=5, y=6)
        expected_output = "[Square] (89) 5/6 - 4\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_all_kwargs_twice(self):
        s = Square(2, 2, 2, 2)
        s.update(id=89, size=3, x=5, y=6)
        s.update(id=33, size=8, x=8, y=8)
        expected_output = "[Square] (33) 8/8 - 8\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_kwargs_size_type(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negetive(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-2)

    def test_update_kwargs_x_type(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-1)

    def test_update_kwargs_y_type(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-2)

class TestSquare_size(unittest.TestCase):
    """unittest for square area method"""

    def test_square_area(self):
        s1 = Square(6)
        self.assertEqual(s1.area(), 36)

class TestSquare_display(unittest.TestCase):
    """unitest for display method."""

    def test_square_disp(self):
        s = Square(3)
        expected_output = "###\n###\n###\n"
        with patch('sys.stdout', new = StringIO()) as out:
            s.display()
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_disp_with_x(self):
        s = Square(3, 1, 0, 1)
        expected_output = " ###\n ###\n ###\n"
        with patch('sys.stdout', new = StringIO()) as out:
            s.display()
            self.assertEqual(out.getvalue(), expected_output)

    def test_square_disp_with_xy(self):
        s = Square(3, 1, 3)
        expected_output = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new = StringIO()) as out:
            s.display()
            self.assertEqual(out.getvalue(), expected_output)


class TestSquare_raises(unittest.TestCase):
    """unittest instantation input."""

    def test_raise_square_str_x(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.x = '10'

    def test_raise_square_str_y(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.y = '10'
    
    def test_raise_square_set_size(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.size = {}
    
    def test_raise_square_set_x(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.x = {1}
    
    def test_raise_square_set_y(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.y = {2}
    
    def test_raise_square_list_size(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.size = [2]
    
    def test_raise_square_list_x(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.x = [2]
    
    def test_raise_square_list_y(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.y = [2]
    
    def test_raise_square_value_size(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            s.size = -2
    
    def test_raise_square_value_x(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            s.x = -2
    def test_raise_square_value_y(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            s.y = -2

class TestSquare_to_Dictonary(unittest.TestCase):
    """Unitest to_dictionsry method"""

    def test_square_to_dict(self):
        s1 = Square(10, 2, 1, 5)
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(s1_dictionary, {'id': 5, 'x': 2, 'y': 1, 'size': 10})

    def test_square_to_dict_2(self):
        s1 = Square(10, 0, 0, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(s1_dictionary, {'id': 1, 'x': 0, 'size': 10, 'y': 0})


if __name__ == '__main__':
    unittest.main()
