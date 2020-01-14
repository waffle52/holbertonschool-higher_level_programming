#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        my_list = [5, 10, 9, 7]
        # tests for biggest num in list
        self.assertEqual(max_integer(my_list), 10)
    def test_empty(self):
        my_list = []
        # tests if list is empty
        self.assertEqual(max_integer(my_list), None)
    def test_oneValue(self):
        my_list = [10]
        # tests if list has only one value
        self.assertEqual(max_integer(my_list), 10)
    def test_float(self):
        my_list = [10, 15, 16.5]
        # tests if will return float
        self.assertEqual(max_integer(my_list), 16.5)
