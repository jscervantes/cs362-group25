import unittest
from task import my_datetime, conv_num
from datetime import datetime
import random


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


class Function1Tests(unittest.TestCase):
    def test_empty_string(self):
        """Test if empty string"""
        num_str = ''
        result = conv_num(num_str)
        self.assertEqual(result, None)

    def test_if_string(self):
        """Test if input is a string"""
        num_str = [1, 2, 3]
        result = conv_num(num_str)
        self.assertEqual(result, None)

    def test_if_number(self):
        """Test if a string returns an integer"""
        num_str = '123456'
        result = conv_num(num_str)
        expected = 123456
        self.assertEqual(result, expected)

    def test_if_negative(self):
        """Test if string returns negative."""
        num_str = "-123"
        result = conv_num(num_str)
        expected = -123
        self.assertEqual(result, expected)

    def test_if_float(self):
        """Test if string is a float."""
        num_str = '-123.45'
        result = conv_num(num_str)
        expected = -123.45
        self.assertEqual(result, expected)


class Function2Tests(unittest.TestCase):
    # Citation:
    # For utcfromtimestamp(): https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp
    # For strftime(): https://docs.python.org/3/library/datetime.html#datetime.date.strftime

    def test1(self):
        """Test edge case of 0 seconds"""
        num_sec = 0
        actual = my_datetime(num_sec)
        expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(actual, expected)

    def test2(self):
        """Test edge case of 12/31/9999"""
        num_sec = 253402300799
        actual = my_datetime(num_sec)
        expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(actual, expected)

    def test3(self):
        """Test example in assignment"""
        num_sec = 9876543210
        actual = my_datetime(num_sec)
        expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(actual, expected)

    def test4(self):
        """Test example in assignment"""
        num_sec = 123456789
        actual = my_datetime(num_sec)
        expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(actual, expected)

    def test5(self):
        """Test example in assignment"""
        num_sec = 201653971200
        actual = my_datetime(num_sec)
        expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(actual, expected)

    def test_random_large_set(self):
        """Random tests that go up to 12/31/9999"""
        tests = 100000
        for i in range(tests):
            num_sec = random.randint(0, 253402300799)
            actual = my_datetime(num_sec)
            expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
            self.assertEqual(actual, expected, msg='num_secs={}'.format(num_sec))

    def test_random_small_set(self):
        """Random tests that run locally but will not go up to year 9999"""
        tests = 100000
        for i in range(tests):
            num_sec = random.randint(0, 9999999999)
            actual = my_datetime(num_sec)
            expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
            self.assertEqual(actual, expected, msg='num_secs={}'.format(num_sec))


if __name__ == '__main__':
    unittest.main()
