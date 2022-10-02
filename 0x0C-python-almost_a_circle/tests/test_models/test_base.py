#!/usr/bin/python3
"""Unit test module."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Define unit test for ...."""

    def test_empty_id(self):
        """Test empty id initilization output."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_empty_id2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nonempty_id(self):
        b3 = Base(10)
        self.assertEqual(b3.id, 10)

#    def test_str_id(self):
#        b4 = Base("10")
#        self.assertEqual(b4.id, '10')
#    def test_save_to_file(self):
#        r1 = Rectangle(10, 7, 2, 8)
#        r2 = Rectangle(2, 4)
#        Rectangle.save_to_file([r1, r2])
#        with open("Rectangle.json", "r") as file:
#            self.assertEqual(file.read(), [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}])
    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])

    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) == list)
    
    def test_dictionary_to_instance(self):
        r1 = Rectangle(3, 5, 1, 4, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_file_to_instance(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        #for square in list_squares_output:
        self.assertEqual(s1.id, 3)
        self.assertEqual(s2.id, 4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.x, 9)
        self.assertEqual(s2.y, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 7)
if __name__ == '__main__':
    unittest.main()

