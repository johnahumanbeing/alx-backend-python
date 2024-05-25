#!/usr/bin/env python3
""" Test utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Test access_nested_map function
    """

    @parameterized.expand(
    [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple, expected: Any):
        """ Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple, expected: Any):
        """ Test access_nested_map function
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)