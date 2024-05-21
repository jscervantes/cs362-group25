import unittest
from task import my_datetime, conv_endian
from datetime import datetime
import random


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


class Function1Tests(unittest.TestCase):
    def test1(self):
        pass


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
        """Test example in assignment"""
        num_sec = 987654321
        actual = my_datetime(num_sec)
        expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
        self.assertEqual(actual, expected)

    def test_random_large_set(self):
        """Random tests that go up to 12/31/9999"""
        tests = 10000
        for i in range(tests):
            num_sec = random.randint(0, 253402300799)
            actual = my_datetime(num_sec)
            expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
            self.assertEqual(actual, expected, msg='num_secs={}'.format(num_sec))

    def test_random_small_set(self):
        """Random tests that can run locally but don't go up to year 9999"""
        tests = 10000
        for i in range(tests):
            num_sec = random.randint(0, 9999999999)
            actual = my_datetime(num_sec)
            expected = datetime.utcfromtimestamp(num_sec).strftime('%m-%d-%Y')
            self.assertEqual(actual, expected, msg='num_secs={}'.format(num_sec))


class Function3Tests(unittest.TestCase):
    def test1(self):
        """Test function returns correct output when endian not 'big' or 'small'"""
        endian = 'other'
        actual = conv_endian(11, endian)
        expected = None
        self.assertEqual(actual, expected)

    def test2(self):
        """Test function handles '0' correctly."""
        actual = conv_endian(0)
        expected = '00'
        self.assertEqual(actual, expected)

    def test3(self):
        """Test function handles example integer correctly. Endian argument not passed.
        Stolen from exploration."""
        actual = conv_endian(954786)
        expected = '0E 91 A2'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
