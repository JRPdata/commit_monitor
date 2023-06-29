import unittest
from unittest.mock import patch
from datetime import datetime

from feed.feed import fetch_rss_feed, check_for_update
from history.history import load_last_updated

class TestFeed(unittest.TestCase):
    def test_fetch_rss_feed(self):
        # Test case for fetch_rss_feed function
        repo_url = "https://github.com/djechlin/fixed-test-repo-frozen-commits"
        feed = fetch_rss_feed(repo_url)

        # Assert that the feed is not empty
        self.assertIsNotNone(feed)
        # Assert that the feed entries are present
        self.assertIn("entries", feed)
        # Assert that the feed entries.updated is present
        self.assertIn("updated", feed["entries"][0])

    @patch('feed.feed.fetch_rss_feed')
    @patch('feed.feed.load_last_updated')
    def test_check_for_update(self, mock_load_last_updated, mock_fetch_rss_feed):
        # Mock the return values for fetch_rss_feed and load_last_updated
        new_updated = '2023-02-23T02:40:06Z'
        mock_fetch_rss_feed.return_value = {
            'entries': [
                {'updated': new_updated}
            ]
        }
        mock_load_last_updated.return_value = '2023-02-23T02:39:29Z'  # Last updated time stored
        last_updated = '2023-02-23T02:39:29Z'

        # Perform the test
        repo_id = 'test'
        repo_url = 'https://github.com/djechlin/fixed-test-repo-frozen-commits'
        result = check_for_update(repo_id, repo_url, last_updated)

        # Assertion
        self.assertEqual(new_updated, result)  # An update is detected

    @patch('feed.feed.fetch_rss_feed')
    @patch('feed.feed.load_last_updated')
    def test_check_for_update_no_update(self, mock_load_last_updated, mock_fetch_rss_feed):
        # Mock the return values for fetch_rss_feed and load_last_updated
        mock_fetch_rss_feed.return_value = {
            'entries': [
                {'updated': '2023-02-23T02:39:29Z'}
            ]
        }
        mock_load_last_updated.return_value = '2023-02-23T02:39:29Z'  # Last updated time stored
        last_updated = '2023-02-23T02:39:29Z'

        # Perform the test
        repo_id = 'test'
        repo_url = 'https://github.com/djechlin/fixed-test-repo-frozen-commits'
        result = check_for_update(repo_id, repo_url, last_updated)

        # Assertion
        self.assertEqual(result, None)  # No update is detected

if __name__ == '__main__':
    unittest.main()
