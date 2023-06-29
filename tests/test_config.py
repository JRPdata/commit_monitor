import unittest
from config.config import load_config, initialize_repositories
import re

class ConfigTestCase(unittest.TestCase):
    def test_load_config(self):
        # Test case for load_config() function
        repo_id = "test"
        expected_config_data = {
            "url": "https://github.com/djechlin/fixed-test-repo-frozen-commits",
            "filters": [re.compile('README.*'), re.compile('^/no-file-matching-this.*')]
        }

        config_data = load_config(repo_id)
        self.assertEqual(config_data, expected_config_data)

    def test_initialize_repositories(self):
        # Test case for initialize_repositories() function
        expected_repositories = [
            ("test", {
                "url": "https://github.com/djechlin/fixed-test-repo-frozen-commits",
                "filters": [re.compile('README.*'), re.compile('^/no-file-matching-this.*')]
            })
        ]

        repositories = initialize_repositories()
        self.assertEqual(repositories, expected_repositories)

if __name__ == '__main__':
    unittest.main()
