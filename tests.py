import unittest
from task import my_datetime, conv_endian, conv_num
from datetime import datetime, timezone
import random


class Function1Tests(unittest.TestCase):
    """Tests for Function 1 conv_num()"""
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

    def test_float(self):
        """Testing different float strings."""
        num_str = "-123."
        result = conv_num(num_str)
        expected = -123.0
        self.assertEqual(result, expected)

    def test_hex(self):
        """Testing hex string function."""
        num_str = "-0xAD4"
        result = conv_num(num_str)
        expected = -2772
        self.assertEqual(result, expected)

    def test_pos_random_integers(self):
        """Random tests using positive integers between 1 and 999999999999."""
        tests = 100000
        for i in range(tests):
            expected = random.randint(0, 999999999999)
            test_string = str(expected)
            actual = conv_num(test_string)
            self.assertEqual(actual, expected)

    def test_pos_random_floats(self):
        """Random tests using positive floats between 1 and 99999999999."""
        tests = 100000
        for i in range(tests):
            expected = random.uniform(0, 99999999999)
            test_string = str(expected)
            actual = conv_num(test_string)
            self.assertEqual(actual, expected)

    def test_pos_random_hex(self):
        """
        Random tests using positive hex numbers with lengths between 1 and
        11.
        """
        tests = 100000
        for i in range(tests):
            length = random.randint(0, 11)
            test_string = ''.join(random.choice('0123456789abcdef')
                                  for _ in range(length))
            try:
                expected = int(test_string, 16)
            except ValueError:
                continue
            test_string = '0x' + test_string
            actual = conv_num(test_string)
            self.assertEqual(actual, expected)

    def test_neg_random_integers(self):
        """
        Random tests using negative integers between 1 and 999999999999.
        """
        tests = 100000
        for i in range(tests):
            expected = -(random.randint(1, 999999999999))
            test_string = str(expected)
            actual = conv_num(test_string)
            self.assertEqual(actual, expected)

    def test_neg_random_floats(self):
        """Random tests using negative floats between 1 and 99999999999."""
        tests = 100000
        for i in range(tests):
            expected = -(random.uniform(1, 99999999999))
            test_string = str(expected)
            actual = conv_num(test_string)
            self.assertEqual(actual, expected)

    def test_neg_random_hex(self):
        """
        Random tests using negative hex numbers with lengths between 1 and 11.
        """
        tests = 100000
        for i in range(tests):
            length = random.randint(0, 11)
            test_string = ''.join(random.choice('0123456789abcdef')
                                  for _ in range(length))
            try:
                expected = -(int(test_string, 16))
            except ValueError:
                continue
            test_string = '-0x' + test_string
            actual = conv_num(test_string)
            self.assertEqual(actual, expected)

    def test_spaces(self):
        """Testing white spaces to see if it returns None"""
        num_str = " 0.123 "
        result = conv_num(num_str)
        expected = None
        self.assertEqual(result, expected)


class Function2Tests(unittest.TestCase):
    """
    Tests for Function 2 my_datetime()
    Citation:
    docs.python.org/3/library/datetime.html#datetime.date.strftime
    """

    def test1(self):
        """Test edge case of 0 seconds"""
        num_sec = 0
        actual = my_datetime(num_sec)
        expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
        expected_formatted = expected.strftime('%m-%d-%Y')
        self.assertEqual(actual, expected_formatted)

    def test2(self):
        """Test edge case of 12/31/9999"""
        num_sec = 253402300799
        actual = my_datetime(num_sec)
        expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
        expected_formatted = expected.strftime('%m-%d-%Y')
        self.assertEqual(actual, expected_formatted)

    def test3(self):
        """Test example in assignment"""
        num_sec = 9876543210
        actual = my_datetime(num_sec)
        expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
        expected_formatted = expected.strftime('%m-%d-%Y')
        self.assertEqual(actual, expected_formatted)

    def test4(self):
        """Test example in assignment"""
        num_sec = 123456789
        actual = my_datetime(num_sec)
        expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
        expected_formatted = expected.strftime('%m-%d-%Y')
        self.assertEqual(actual, expected_formatted)

    def test5(self):
        """Test example in assignment"""
        num_sec = 201653971200
        actual = my_datetime(num_sec)
        expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
        expected_formatted = expected.strftime('%m-%d-%Y')
        self.assertEqual(actual, expected_formatted)

    def test6(self):
        """Test 2/29 in leap year"""
        num_sec = 1709193600
        actual = my_datetime(num_sec)
        expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
        expected_formatted = expected.strftime('%m-%d-%Y')
        self.assertEqual(actual, expected_formatted)

    def test_random_large_set(self):
        """Random tests that go up to 12/31/9999"""
        tests = 100000
        for i in range(tests):
            num_sec = random.randint(0, 253402300799)
            actual = my_datetime(num_sec)
            expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
            expected_formatted = expected.strftime('%m-%d-%Y')
            self.assertEqual(actual, expected_formatted)

    def test_random_small_set(self):
        """Random tests that run locally but will not go up to year 9999"""
        tests = 100000
        for i in range(tests):
            num_sec = random.randint(0, 9999999999)
            actual = my_datetime(num_sec)
            expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
            expected_formatted = expected.strftime('%m-%d-%Y')
            self.assertEqual(actual, expected_formatted)

    def test_datetime(self):
        """Testing my partner's function"""
        for _ in range(1000):
            num_sec = random.randint(0, 253402300799)
            actual = my_datetime(num_sec)
            expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
            expected_formatted = expected.strftime('%m-%d-%Y')
            self.assertEqual(actual, expected_formatted)

    def test_edge_case(self):
        """Testing my_datetime() with a timestamp close to the epoch."""
        num_sec = 60
        actual = my_datetime(num_sec)
        expected = datetime.fromtimestamp(num_sec, tz=timezone.utc)
        expected_formatted = expected.strftime('%m-%d-%Y')
        self.assertEqual(actual, expected_formatted)


class Function3Tests(unittest.TestCase):
    """Tests for Function 3 conv_endian()"""
    def test1(self):
        """
        Test function returns correct output when endian not 'big' or
        'small'
        """
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
        """
        Test function handles example integer correctly.
        Endian argument not passed.
        From exploration.
        """
        actual = conv_endian(954786)
        expected = '0E 91 A2'
        self.assertEqual(actual, expected)

    def test4(self):
        """
        Test function handles negative integer correctly.
        Endian argument not passed.
        From exploration.
        """
        actual = conv_endian(-954786)
        expected = '-0E 91 A2'
        self.assertEqual(actual, expected)

    def test5(self):
        """
        Test function handles 'big' endian argument with positive integer.
        From exploration.
        """
        actual = conv_endian(954786, 'big')
        expected = '0E 91 A2'
        self.assertEqual(actual, expected)

    def test6(self):
        """
        Test function handles 'little' endian argument with positive integer.
        From exploration.
        """
        actual = conv_endian(954786, 'little')
        expected = 'A2 91 0E'
        self.assertEqual(actual, expected)

    def test7(self):
        """
        Test function handles 'little' endian argument with negative integer.
        From exploration.
        """
        actual = conv_endian(-954786, 'little')
        expected = '-A2 91 0E'
        self.assertEqual(actual, expected)

    def test_random_pos_big(self):
        """
        Random tests using positive ints between 1 and 99999999999
        and endian is big
        """
        tests = 1000000
        for i in range(tests):
            hex_num_test = random.randint(0, 99999999999)

            actual = conv_endian(hex_num_test)

            # Convert int to hex using hex() and format to match conv_endian()
            hex_expected = hex(hex_num_test).lstrip("0x").upper()

            hex_str = '{}'.format(hex_expected)

            if len(hex_str) % 2 != 0:
                hex_str = '0{}'.format(hex_str)

            hex_bytes = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]

            expected = ' '.join(hex_bytes)

            self.assertEqual(actual, expected)

    def test_random_neg_big(self):
        """
        Random tests using negative ints between 0 and 99999999999
        and endian is big
        """
        tests = 1000000
        for i in range(tests):
            hex_num_test = random.randint(0, 99999999999)

            actual = conv_endian(hex_num_test * -1)

            # Convert int to hex using hex() and format to match conv_endian()
            hex_expected = hex(hex_num_test).lstrip("0x").upper()
            hex_str = '{}'.format(hex_expected)

            if len(hex_str) % 2 != 0:
                hex_str = '0{}'.format(hex_str)

            hex_bytes = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]

            expected = ' '.join(hex_bytes)

            expected = '-{}'.format(expected)

            self.assertEqual(actual, expected)

    def test_random_pos_little(self):
        """
        Random tests using positive ints between 0 and 99999999999
        and endian is little
        """
        tests = 1000000
        for i in range(tests):
            hex_num_test = random.randint(0, 99999999999)

            actual = conv_endian(hex_num_test, 'little')

            # Convert int to hex using hex() and format to match conv_endian()
            hex_expected = hex(hex_num_test).lstrip("0x").upper()
            hex_str = '{}'.format(hex_expected)

            if len(hex_str) % 2 != 0:
                hex_str = '0{}'.format(hex_str)

            hex_bytes = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]

            hex_bytes.reverse()

            expected = ' '.join(hex_bytes)

            self.assertEqual(actual, expected)

    def test_random_neg_little(self):
        """
        Random tests using negative ints between 0 and 99999999999
        and endian is little
        """
        tests = 1000000
        for i in range(tests):
            hex_num_test = random.randint(0, 99999999999)

            actual = conv_endian(hex_num_test * -1, 'little')

            # Convert int to hex using hex() and format to match conv_endian()
            hex_expected = hex(hex_num_test).lstrip("0x").upper()

            hex_str = '{}'.format(hex_expected)

            if len(hex_str) % 2 != 0:
                hex_str = '0{}'.format(hex_str)

            hex_bytes = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]

            hex_bytes.reverse()

            expected = ' '.join(hex_bytes)

            expected = '-{}'.format(expected)

            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
