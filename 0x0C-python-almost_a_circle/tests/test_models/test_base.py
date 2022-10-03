#!/usr/bin/python3
"""Unit test module."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantation(unittest.TestCase):
    """Define unittest for base instantation"""

    def test_2empty_arg(self):
        """Test empty id initilization output."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_3empty_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_empty_id_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_public_id(self):
        b1 = Base(12)
        b1.id = 2
        self.assertEqual(b1.id, 2)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)


class TestBase_from_json_string(unittest.TestCase):
    """Test class method from_json_string."""

    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
    
    def test_from_json_string_one_Rec(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(list_input, list_output)

    def test_from_json_string_type(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) == list)

    def test_from_json_string_type(self):
        list_input = [
                    {'id': 89, 'size': 4, 'x': 2},
                    {'id': 7, 'size': 1, 'x': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)


class TestBase_dictionary_to_instance(unittest.TestCase):
    """Test from dictionary to instance initilizer module."""

    def test_dictionary_to_instance_equality(self):
        r1 = Rectangle(3, 5, 1, 4, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_dictionary_to_instance(self):
        r1 = Rectangle(3, 5, 1, 4, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1_dictionary, r2.to_dictionary())

class TestBase_save_to_file(unittest.TestCase):
    """Unitest for save to file module."""

    @classmethod
    def TearDown(self):
        """Delete created file after each test."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

        try:
            os.remove("Square.json")
        except IOError:
            pass

        try:
            os.Remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_Rec(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
                self.assertEqual(len(file.read()), 100)

    def test_save_to_file_two_Rec(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(3, 4, 5, 5, 7)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
                self.assertEqual(len(file.read()), 200)

    def test_save_to_file_one_Squ(self):
        s1 = Square(2, 3, 4, 5)
        Rectangle.save_to_file([s1])
        with open("Square.json", "r") as file:
                self.assertEqual(len(file.read()), 240)

    def test_save_to_file_two_Squ(self):
        s1 = Square(1, 2, 4, 5)
        s2 = Square(4, 3, 2, 6)
        Rectangle.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
                self.assertEqual(len(file.read()), 240)

    def test_save_to_file_overwrite_Rec(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        r1 = Rectangle(1, 2)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
                self.assertEqual(len(file.read()), 101)

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
                self.assertEqual(file.read(), "[]")

    def test_save_to_file_emptyList_rec(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
                self.assertEqual(file.read(), "[]")

    def test_save_to_file_multiArg_Rec(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([1], 3)


if __name__ == '__main__':
    unittest.main()

