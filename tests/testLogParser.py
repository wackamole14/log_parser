import unittest
from log_parser import parse_log_line, search_log


class TestLogParser(unittest.TestCase):
    initial_time = 1565648174257
    one_hour = 3600000
    four_minutes = 240000

    def setUp(self):
        self.log_file = 'input-file-10000__1_.txt'
        with open(self.log_file, 'w') as f:
            f.write(str(self.initial_time + self.four_minutes) + " Eisha Aashita\n")
            f.write(str(self.initial_time - self.four_minutes) + " Klein Nykeemah\n")
            f.write(str(self.initial_time + self.one_hour) + " Eisha Klein\n")
            f.write(str(self.initial_time + (self.one_hour * 2) + self.four_minutes) + " Nykeemah Aashita\n")
            f.write(str(self.initial_time + (self.one_hour*2)) + " Nykeemah Eron\n")

    def test_parse_log_line_valid(self):
        """
        Test that a valid log line is correctly parsed into a tuple.
        """
        line = "1565648174257 Eisha Aashita\n"
        expected = (1565648174257, "Eisha", "Aashita")
        self.assertEqual(parse_log_line(line), expected)

    def test_parse_log_line_invalid(self):
        """
        Test that an invalid log line raises a ValueError.
        """
        line = "invalid log line"
        with self.assertRaises(ValueError):
            parse_log_line(line)

    def test_search_log_ignore_out_of_order_record_start(self):
        """
        Test that records out of the specified start time range are ignored even.
        """
        result = search_log(self.log_file, self.initial_time, self.initial_time + self.one_hour, 'Klein')
        expected = ['Eisha']
        self.assertEqual(expected, result)

    def test_search_log_include_record_out_of_order_start(self):
        """
        Test that records within the specified start time range are included.
        """
        result = search_log(self.log_file, self.initial_time - self.four_minutes, self.initial_time + self.one_hour, 'Klein')
        expected = ['Nykeemah', 'Eisha']
        self.assertEqual(expected, result)

    def test_search_log_exclude_record_out_of_order_end(self):
        """
        Test that records out of the specified end time range are excluded.
        """
        result = search_log(self.log_file, self.initial_time, self.initial_time + (self.one_hour*2), 'Nykeemah')
        expected = ['Eron']
        self.assertEqual(expected, result)

    def test_search_log_include_record_out_of_order_end(self):
        """
        Test that records within the specified end time range are included.
        """
        result = search_log(self.log_file, self.initial_time, (self.initial_time + (self.one_hour*2)) + self.four_minutes, 'Nykeemah')
        expected = ['Aashita', 'Eron']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()