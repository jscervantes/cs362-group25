def conv_num(num_str):
    """Takes in a string and converts it into a base 10 number,
    and returns it."""

    # Check if the string is empty.
    if len(num_str) == 0:
        return None

    # Check if the string is a string.
    if not isinstance(num_str, str):
        return None

    # Strip leading and trailing whitespace from string.
    num_str = num_str.strip()

    # Check if the passed string is a number.
    if is_valid_num(num_str):
        # if it is, then convert the string to a number.
        return str_to_num(num_str)
    else:
        return None


def is_valid_num(num_str):
    """Helper function to return true if the string is a number."""
    # Check if negative.
    if num_str[0] == '-':
        # strip string of negative sign.
        num_str = num_str[1:]
        # check to see if string is empty.
        if len(num_str) == 0:
            return False

    # Check for valid decimal points.
    if num_str.count('.') > 1:
        return False

    # Check if the string only has a decmial point.
    if num_str == '.':
        return False

    # Iterate through string to see if it matches the numbers.
    for char in num_str:
        if char not in '0123456789.':
            return False
    return True


def str_to_num(num_str):
    """Helper function to convert the string to a number"""
    # Track negative flag.
    is_negative = False
    # If negative mark flag true.
    if num_str[0] == '-':
        is_negative = True
        # strip negative sign.
        num_str = num_str[1:]

    # Check if the number is a float.
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

    # Store the converted fractional part.
    if fraction_part:
        # store the fraction number.
        frac_num = 0
        # Keep track of pos to the right of decimal.
        frac_pos = 1

        # iterate through the fraction_part.
        for char in fraction_part:
            # Converts char into a digit.
            digit = ord(char) - ord('0')
            # Keep track of base 10 position.
            frac_num = frac_num * 10 + digit
            # Every iteration the fraction position is stored.
            frac_pos *= 10
        # store int number + (frac_num/frac_pos) in num.
        num += frac_num / frac_pos

    # if string is negative, return negative num.
    if is_negative:
        return -num
    return num


def my_datetime(num_sec):
    """Takes an integer value that represents the number of seconds
        since the epoch (01/01/1970) and returns the date as a string
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
    """Determines if a year is a leap year.
    Returns True if a leap year and False otherwise
    """
    if year % 100 == 0 and year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False


def find_year(days_remaining):
    """Determines the year of the new date and
    returns the year and the remaining days
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
    """Determines the month of the new date and
    returns the month and the remaining days
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
    Takes an integer num and converts it to a hexadecimal number. Endian type is determined by endian flag.
    """
    if endian not in ('big', 'little'):
        return None

    # Convert the integer into hexidecimal
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

    # Split the string into bytes
    hex_bytes = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]

    # Join bytes with space between!
    return_hex = ' '.join(hex_bytes)

    # Manually reorder the bytes if the endian type is little

    return return_hex
