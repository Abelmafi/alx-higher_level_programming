#!/usr/bin/python3
"""Unitest module for Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle_instantation(unittest.TestCase):
    """Test cases."""

    def test_rectangle_emptyId(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(5, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_uniqueId(self):
        r1 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r1.id, 5)

    def test_raise_except_str_width(self):
        r2 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r2.width = '10'

    def test_raise_except_str_height(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.height = '1'

    def test_raise_except_str_x(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.x = '11'

    def test_raise_except_str_y(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.y = 'hi'

    def test_raise_except_value_width(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(ValueError):
            r5.width = 0

    def test_raise_except_value_height(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(ValueError):
            r5.height = -2

    def test_raise_except_value_x(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(ValueError):
            r5.x = -1

    def test_raise_except_value_y(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(ValueError):
            r5.y = -1
    
    def test_raise_except_value_width_set(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.width = {}

    def test_raise_except_value_height_set(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.height = {}

    def test_raise_except_value_x_set(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.x = {}

    def test_raise_except_value_y_set(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.y = {}

    def test_raise_except_value_width_list(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.width = [2]

    def test_raise_except_value_height_list(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.height = [1]

    def test_raise_except_value_x_list(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.x = [3]

    def test_raise_except_value_y_list(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.y = [1]

    def test_raise_except_value_width_float(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.width = 2.2

    def test_raise_except_value_height_float(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.height = 3.1

    def test_raise_except_value_x_float(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.x = 2.5

    def test_raise_except_value_y_float(self):
        r5 = Rectangle(1, 2, 1, 3, 4)
        with self.assertRaises(TypeError):
            r5.y = 2.3

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__y)

    def test_width_setter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.width = 10
        self.assertEqual(r1.width, 10)

    def test_width_getter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)

    def test_height_setter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.height = 10
        self.assertEqual(r1.height, 10)

    def test_height_getter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.height, 2)

    def test_x_setter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.x = 10
        self.assertEqual(r1.x, 10)

    def test_x_getter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.x, 3)

    def test_y_setter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.y = 10
        self.assertEqual(r1.y, 10)

    def test_y_getter(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.y, 4)


class TestRectangle_area_display(unittest.TestCase):
    """Unittest area attribute or rectangle class..."""

    def test_area(self):
        r1 = Rectangle(3, 2, 1, 1, 1)
        self.assertEqual(r1.area(), 6)
    
    def test_width_height_x__str__(self):
        r = Rectangle(4, 5, 2)
        expected_output = "[Rectangle] ({}) 2/0 - 4/5\n".format(r.id)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_all___str__(self):
        r = Rectangle(5, 5, 1, 0, 2)
        expected_output = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(r.__str__(), expected_output)
    
    #Test display method
    def test_display_0(self):
        r1 = Rectangle(4, 4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_x(self):
        r1 = Rectangle(4, 4, 1)
        expected_output = " ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_y(self):
        r1 = Rectangle(4, 4, 0, 2)
        expected_output = "\n\n####\n####\n####\n####\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_x_y(self):
        r9 = Rectangle(2, 3, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r9.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
    
    def test_update_0(self):
        r2 = Rectangle(2, 2, 2, 2, 2)
        r2.update(89)
        expected_output = "[Rectangle] (89) 2/2 - 2/2\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), expected_output)


class TestRectangle_update(unittest.TestCase):
    """Unittest Rectangle update."""

    def test_update_zero_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update()
        self.assertEqual("[Rectangle] (2) 2/2 - 2/2", str(r))

    def test_update_id_width_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(89, 3)
        expected_output = "[Rectangle] (89) 2/2 - 3/2\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_all_args(self):
        r = Rectangle(2, 2, 2, 2)
        r.update(89, 3, 4, 5, 6)
        expected_output = "[Rectangle] (89) 5/6 - 3/4\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_all_args_twice(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(89, 3, 5, 6, 7)
        r.update(33, 8, 8, 8, 8)
        expected_output = "[Rectangle] (33) 8/8 - 8/8\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_args_width_type(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negetive(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -1)

    def test_update_args_height_type(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 2, 0)

    def test_update_args_height_negetive(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -3)

    def test_update_args_x_type(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 2, "invalid")

    def test_update_args_x_negetive(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 2, 2, -2)

    def test_update_args_y_type(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 2, 3,"invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 2, 2, 3, -2)

class TestRectangle_kwargs(unittest.TestCase):
    """unittest inputs with kwargs."""

    def test_update_id_kwarg(self):
        r = Rectangle(10, 10, 10, 10, 2)
        r.update(id=3)
        expected_output = "[Rectangle] (3) 10/10 - 10/10\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_id_width_kwarg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=2, id=89)
        expected_output = "[Rectangle] (89) 10/10 - 2/10\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_id_width_height_kwarg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=2, height=5, id=89)
        expected_output = "[Rectangle] (89) 10/10 - 2/5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)
    
    def test_update_except_y_kwarg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=2, height=5, x=3, id=89)
        expected_output = "[Rectangle] (89) 3/10 - 2/5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)
    
    def test_update_all_kwarg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, height=5, x=3, id=89)
        expected_output = "[Rectangle] (89) 3/1 - 2/5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_twice_kwarg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, height=5, x=3, id=89)
        r.update(x=9, width=9, height=9, y=9)
        expected_output = "[Rectangle] (89) 9/9 - 9/9\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_kwargs_width_type(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(id=89, width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(id=89, width=0)

    def test_update_kwargs_width_negetive(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(id=89, width=-1)

    def test_update_kwargs_height_type(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(id=89, height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(id=89, height=0)

    def test_update_kwargs_height_negetive(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(id=89, height=-3)

    def test_update_kwargs_x_type(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(id=89, x="invalid")

    def test_update_kwargs_x_negetive(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(id=89, x=-2)

    def test_update_args_y_type(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(id=89, y="invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(id=89, y=-2)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unitest tp_dictionary converter method test."""
    
    def test_to_dict_output(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_output = {'x': 3, 'y': 4, 'width': 1, 'height': 2, 'id': 5}
        self.assertDictEqual(r.to_dictionary(), expected_output)

    def test_to_dict_copy_attribute_value(self):
        r = Rectangle(2, 3, 4, 5, 6)
        r2 = Rectangle(8, 8, 8, 8, 8)
        r2.update(**r.to_dictionary())
        self.assertNotEqual(r, r2)

    def test_to_dict_copy_attribute_value2(self):
        r = Rectangle(2, 3, 4, 5, 6)
        r2 = Rectangle(8, 8, 8, 8, 8)
        r2.update(**r.to_dictionary())
        self.assertFalse(r is r2)

if __name__ == "__main__":
    unittest.main()


