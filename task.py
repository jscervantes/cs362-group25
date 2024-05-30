def conv_num(num_str):
    """Takes in a string and converts it into a base 10 number,
    and returns it."""

    # Check if the string is empty.
    if len(num_str) == 0:
        return None

    is_negative = False
    if num_str[0] == '-':
        is_negative = True
        num_str = num_str[1:]

    # Check if the string is a string.
    if not isinstance(num_str, str):
        return None

    # Check if the string is a valid number.
    if is_valid_num(num_str):
        number = str_to_num(num_str)
        if is_negative:
            return -number
        return number
    elif is_valid_hex(num_str):
        # if a valid hex, convert string to a number.
        number = hex_to_num(num_str)
        if is_negative:
            return -number
        return number
    else:
        return None


def is_valid_num(num_str):
    """Helper function to return true if the string is a number."""
    # Check for valid decimal points.
    if num_str.count('.') > 1:
        return False

    # Check if the string only has a decimal point.
    if num_str == '.':
        return False

    # Iterate through string to see if it matches the numbers.
    for char in num_str:
        if char not in '0123456789.':
            return False
    return True


def is_valid_hex(num_str):
    """Helper function to return true if the string is a valid hexadecimal."""
    # Check if the string has the hexadecimal prefix.
    if len(num_str) > 2 and num_str[0] == '0' and (num_str[1] == 'x' or
                                                   num_str[1] == 'X'):
        hex_part = num_str[2:]
        # Iterate through the hex_part to see if is valid.
        for char in hex_part:
            if char not in '0123456789abcdefABCDEF':
                return False
        return True
    return False


def str_to_num(num_str):
    """Helper function to convert the string to a number"""
    if '.' in num_str:
        # Split the string at the "." and assign variables.
        int_part, fraction_part = num_str.split('.')
    else:
        int_part, fraction_part = num_str, ''

    # Store the converted integer part.
    num = 0
    for char in int_part:
        # Converts the character from ASCII to a digit
        digit = ord(char) - ord('0')
        num = num * 10 + digit

    if fraction_part:
        frac_num = 0
        # Keep track of pos to the right of decimal.
        frac_pos = 1

        # iterate through the fraction_part.
        for char in fraction_part:
            digit = ord(char) - ord('0')
            frac_num = frac_num * 10 + digit
            frac_pos *= 10
        # store int number + (frac_num/frac_pos) in num.
        num += frac_num / frac_pos

    # if num has a "." make it a float.
    if '.' in num_str:
        num = num * 1.0
    return num


def hex_to_num(num_str):
    """Helper function to convert a valid hexadecimal string
    to a base 10 number."""

    # Map to match the hexadecimal value to it's number.
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
               'f': 15, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    hex_part = num_str[2:]
    decimal_number = 0
    # Iterate through the string and verify if it is in the hex_map.
    for char in hex_part:
        if char in hex_map:
            # Convert from hexadecimal to base 10 number.
            decimal_number = decimal_number * 16 + hex_map[char]
        else:
            return None
    return decimal_number


def my_datetime(num_sec):
    """
    Takes an integer value that represents the number of seconds since the
    epoch (01/01/1970) and returns the date as a string
    """

    # Calculates the number of days
    year_days_remaining = (num_sec/86400)

    year, month_days_remaining = find_year(year_days_remaining)

    month, days_remaining = find_month(month_days_remaining, year)

    day = int(days_remaining) + 1

    # Format months and days
    month = '{:02d}'.format(month)
    day = '{:02d}'.format(day)

    return '{}-{}-{}'.format(month, day, year)


def leap_year(year):
    """
    Determines if a year is a leap year.
    Returns True if a leap year and False otherwise.
    """

    if year % 100 == 0 and year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False


def find_year(days_remaining):
    """
    Determines the year of the new date and returns the year and
    the remaining days.
    """

    # Iterates through each year until days remaining are less than a full year
    year = 1970
    while ((leap_year(year) is True and days_remaining >= 366) or
           (leap_year(year) is False and days_remaining >= 365)):
        if leap_year(year):
            days_remaining -= 366
            year += 1
        else:
            days_remaining -= 365
            year += 1

    return year, days_remaining


def find_month(days_remaining, year):
    """
    Determines the month of the new date and returns the month and
    the remaining days.
    """

    # Determines leap year and corresponding number of days for each month
    if leap_year(year):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Iterates each month until days remaining are less than a full month
    for month in range(len(days_in_month)):
        if days_remaining >= days_in_month[month]:
            days_remaining -= days_in_month[month]
        else:
            return month + 1, days_remaining


def conv_endian(num, endian='big'):
    """
    Takes an integer num and converts it to a hexadecimal number. Endian type
    is determined by endian flag.
    """
    if endian not in ('big', 'little'):
        return None

    is_neg = num < 0

    num = abs(num)

    hex_str = conv_hex(num)
    return_hex = split_bytes(hex_str, endian)

    # Set sign of return_hex
    if is_neg:
        return_hex = '-' + return_hex

    return return_hex


def conv_hex(num):
    """
    Helper function for conv_endian. Takes integer, returns padded
    hex string.
    """
    # Convert the integer into hexadecimal
    hex_chars = '0123456789ABCDEF'
    hex_str = ''
    if num == 0:
        hex_str = '0'

    # Add converted remainders to hex_str in reverse order
    while num > 0:
        hex_str = hex_chars[num % 16] + hex_str
        num //= 16

    # Ensure the string has even number of characters, padding if needed
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str

    return hex_str


def split_bytes(hex_str, endian):
    """
    Helper function for conv_endian. Takes unordered and unsplit hex string
    and returns hex string split into bytes and ordered by endianess.
    """

    # Split the string into bytes
    hex_bytes = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]

    # Manually reorder the bytes if the endian type is little
    if endian == 'little':
        hex_bytes.reverse()

    # Join bytes with space between!
    return ' '.join(hex_bytes)
