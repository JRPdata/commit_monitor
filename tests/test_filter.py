import unittest
import re
from filter.filter import filter_files


class TestFilter(unittest.TestCase):
    def test_filter_files(self):
        # Sample complete file list
        complete_file_list = [
            'a.txt',
            'b.py',
            'README.md'
        ]

        # Sample file filters
        file_filters = [re.compile('^a.*'), re.compile('.*RANDOM-NOT-MATCHING.*')]

        # Perform the filtering
        filtered_files = filter_files(complete_file_list, file_filters)

        # Assertion
        expected_filtered_files = [
            'a.txt'
        ]
        self.assertCountEqual(filtered_files, expected_filtered_files)
        self.assertEqual(filtered_files, expected_filtered_files)


if __name__ == '__main__':
    unittest.main()
