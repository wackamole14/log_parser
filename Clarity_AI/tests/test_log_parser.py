import unittest
from log_parser import search_log

class TestLogParser(unittest.TestCase):
    def setUp(self):
        self.log_file = 'input-file-10000__1_.txt'

    def test_search_log(self):
        result = search_log(self.log_file, 1565648174257, 1565661461356, 'Eisha')
        expected = ['Aashita', 'Klein','Nykeemah']  # Adjust this based on the actual expected output from your file
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
