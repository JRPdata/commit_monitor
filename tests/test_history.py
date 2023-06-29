import unittest
from history import history

class HistoryTestCase(unittest.TestCase):

    def setUp(self):
        history.initialize_history_directory()

    def test_last_updated(self):
        repo_id = "test"
        updated_time = "2023-02-23T02:40:06Z"

        # Save and load last updated time
        history.save_last_updated(repo_id, updated_time)
        loaded_updated_time = history.load_last_updated(repo_id)

        # Assert that loaded updated time matches the saved value
        self.assertEqual(loaded_updated_time, updated_time)

    def test_commits(self):
        repo_id = "test"
        commits = ["cc3dad4584a2a4335ef158a0537135a1b78eb0a0", "ea2db7abcba2a3ac992c0cd338429cef50bf48eb"]

        # Save and load commits
        history.save_commits(repo_id, commits)
        loaded_commits = history.load_commits(repo_id)

        # Assert that loaded commits match the saved value
        self.assertEqual(loaded_commits, commits)

if __name__ == "__main__":
    unittest.main()
