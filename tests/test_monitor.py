import unittest
from unittest.mock import patch
from monitor import monitor
from config import config
from github_api import github_api
from feed import feed
from filter import filter
from notify import notify
import re

class MonitorRepositoriesTestCase(unittest.TestCase):
    @patch('config.config.initialize_repositories')
    @patch('github_api.github_api.get_complete_file_list')
    @patch('feed.feed.check_for_update')
    @patch('filter.filter.filter_files')
    @patch('notify.notify.create_notification_message')
    @patch('notify.notify.send_notification')
    def test_monitor_repositories(self, mock_send_notification, mock_create_notification_message,
                                   mock_filter_files, mock_check_for_update,
                                   mock_get_complete_file_list, mock_initialize_repositories):
    # Mocked data for initialization
        repo_id = 'test'
        repo_url = 'https://github.com/djechlin/fixed-test-repo-frozen-commits'
        ntfy_url = 'http://127.0.0.1:80'
        retvalue = [(repo_id, {'url': repo_url, 'filters': []})]
        mock_initialize_repositories.return_value = [(repo_id, {'url': repo_url, 'filters': [re.compile('README.*')]})]

        # Mocked data for update detection
        mock_check_for_update.return_value = '2023-02-23T02:40:06Z'

        # Mocked data for get_complete_file_list
        mock_get_complete_file_list.return_value = ['a.txt', 'README.md']

        # Mocked data for file filtering
        mock_filter_files.return_value = 'README.md'

        # Mocked data for notification creation
        mock_create_notification_message.return_value = 'README.md'

        # Call the monitor_repositories function
        monitor.monitor_repositories()

        # Assert the function calls and behavior
        mock_initialize_repositories.assert_called_once()
        mock_check_for_update.assert_called_once()
        mock_get_complete_file_list.assert_called_once()
        mock_filter_files.assert_called_once()
        mock_create_notification_message.assert_called_once_with(repo_id, 'README.md')
        mock_send_notification.assert_called_once_with(repo_id, ntfy_url, 'README.md')

if __name__ == '__main__':
    unittest.main()
