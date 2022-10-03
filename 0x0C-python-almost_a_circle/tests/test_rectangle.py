#!/usr/bin/python3
"""Unitest module for Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases."""

    @unittest.skip("Skipping incremental id value test")
    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 0, 0, 12)
        r3 = Rectangle(5, 5)
        r4 = Rectangle(2, 3)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 4)

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

    def test_area(self):
        r6 = Rectangle(3, 2, 1, 1, 1)
        r7 = Rectangle(8, 5, 5, 7, 4)
        self.assertEqual(r7.area(), 40)
        self.assertEqual(r6.area(), 6)
    
    def test_display_0(self):
        r5 = Rectangle(4, 4, 0, 0, 2)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r5.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_0_2(self):
        r5 = Rectangle(1, 1, 0, 0, 2)
        expected_output = "#\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r5.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display__str__(self):
        r5 = Rectangle(4, 5, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r5)
            self.assertEqual(fake_out.getvalue(), expected_output)\

    def test_display__str__2(self):
        r9 = Rectangle(5, 5, 1, 0, 2)
        expected_output = "[Rectangle] (2) 1/0 - 5/5\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r9)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_1(self):
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

    def test_update_0_2(self):
        r2 = Rectangle(2, 2, 2, 2, 2)
        r2.update(89, 3)
        expected_output = "[Rectangle] (89) 2/2 - 3/2\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_0_3(self):
        r2 = Rectangle(2, 2, 2, 2)
        r2.update(89, 3, 4, 5, 6)
        expected_output = "[Rectangle] (89) 5/6 - 3/4\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update_1(self):
        r2 = Rectangle(10, 10, 10, 10, 2)
        r2.update(height=1, width=1, x=2)
        expected_output = "[Rectangle] (2) 2/10 - 1/1\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), expected_output)

        r2.update(y=1, width=2, x=3, id=89)
        expected_output = "[Rectangle] (89) 3/1 - 2/1\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), expected_output)



