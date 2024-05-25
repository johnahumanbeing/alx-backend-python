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


class TestGetJson(unittest.TestCase):
    """ Test get_json function
    """

    @parameterized.expand(
        [
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ]
    )
    @patch("request.get")
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
        ) -> None:
        """ Test get_json function
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Test memoize function
    """

    def test_memoize(self) -> None:
        """ Test memoize function
        """

        class TestClass:
            """ TestClass
            """

            def a_method(self) -> int:
                """ a_method
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """ a_property
                """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked.assert_called_once()
