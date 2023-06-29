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

if __name__ == "__main__":
    unittest.main()
