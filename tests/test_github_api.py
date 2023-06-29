import unittest
from unittest.mock import patch
from github_api.github_api import get_complete_file_list


class TestGitHubAPI(unittest.TestCase):
    @patch('github_api.github_api.fetch_commits')
    @patch('github_api.github_api.fetch_commit')
    def test_get_complete_file_list(self, mock_fetch_commit, mock_fetch_commits):
        # Mock the return values for fetch_commits and fetch_commit
        mock_fetch_commits.return_value = [
            {'sha': 'ea2db7abcba2a3ac992c0cd338429cef50bf48eb'},
            {'sha': 'cc3dad4584a2a4335ef158a0537135a1b78eb0a0'}

        ]
        mock_fetch_commit.side_effect = [
            {'files': [{'filename': 'a.txt'}]},
            {'files': [{'filename': 'README.md'}]}
        ]

        # Perform the test
        repo_url = 'https://github.com/djechlin/fixed-test-repo-frozen-commits'
        repo_id = 'test'
        result = get_complete_file_list(repo_url, repo_id)

        # Assertions
        expected_result = list(set(['a.txt', 'README.md']))
        self.assertEqual(result, expected_result)

        mock_fetch_commits.assert_called_once_with(repo_url, repo_id)
        mock_fetch_commit.assert_has_calls([
            unittest.mock.call(repo_url, 'ea2db7abcba2a3ac992c0cd338429cef50bf48eb'),
            unittest.mock.call(repo_url, 'cc3dad4584a2a4335ef158a0537135a1b78eb0a0')

        ])


if __name__ == '__main__':
    unittest.main()
