#!/usr/bin/env python3
""" Test client module.
"""
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
import unittest
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient class.
    """
    @parameterized.expand(
        [
        ("google"),
        ("abc")
    ]
    )
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """ Test GithubOrgClient.org method.
        """
        mock_get_json.return_value = TEST_PAYLOAD
        client = GithubOrgClient(org)
        self.assertEqual(client.org, TEST_PAYLOAD)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """ Test GithubOrgClient._public_repos_url method.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            test_org = {"repos_url": "http://test.com"}
            mock_org.return_value = test_org
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, test_org["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test GithubOrgClient.public_repos method.
        """
        test_repos = [{"name": "test"}]
        mock_get_json.return_value = test_repos
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://test.com"
            client = GithubOrgClient("test")
            self.assertEqual(client.public_repos(), test_repos)
            mock_get_json.assert_called_once()
