import unittest
import shlex
from unittest.mock import patch
from config.config import load_notify
from notify.notify import create_notification_message, send_notification

class TestNotification(unittest.TestCase):
    def test_create_notification_message(self):
        # Test case for create_notification_message function
        repo_id = "test"
        filtered_files = ["a.txt"]

        # Call the function
        message = create_notification_message(filtered_files)

        # Assertion
        expected_message = "a.txt"
        self.assertEqual(message, expected_message)

    @patch('notify.notify.subprocess.run')
    def test_send_notification(self, mock_subprocess_run):
        # Mock the subprocess.run() function
        mock_subprocess_run.return_value.returncode = 0

        # Test data
        repo_id = "test"
        ntfy_url = "https://127.0.0.1"
        message = "a.txt"

        # Perform the test
        send_notification(repo_id, ntfy_url, message)

        # Assertion
        expected_command = shlex.split(f"ntfy publish {ntfy_url}/{repo_id} '{message}'")
        mock_subprocess_run.assert_called_once_with(
            expected_command,
            check=True
        )

if __name__ == '__main__':
    unittest.main()
