def conv_num(num_str):
    """Takes in a string and converts it into a base 10 number, and returns it."""
    pass


def my_datetime(num_sec):
    """Takes an integer value that represents the number of seconds
        since the epoch (01/01/1970) and returns the date as a string
        """

    # Calculates the number of days
    year_days_remaining = (num_sec/86400)

    # Calculates the year and the remaining days
    year, month_days_remaining = find_year(year_days_remaining)

    # Calculates the month and the remaining days
    month, days_remaining = find_month(month_days_remaining, year)

    # Calculates the day
    day = int(days_remaining) + 1

    # Adding padded 0s
    month = '{:02d}'.format(month)
    day = '{:02d}'.format(day)

    return '{}-{}-{}'.format(month, day, year)


def leap_year(year):
    """Determines if a year is a leap year.
    Returns True if a leap year and False otherwise
    """

    # Leap year if divided by 100 and 400
    if year % 100 == 0 and year % 400 == 0:
        return True

    # Non-leap year if divided by 100
    if year % 100 == 0:
        return False

    # Leap year if divided by 4
    if year % 4 == 0:
        return True

    return False


def find_year(days_remaining):
    """Determines the year of the new date and returns the year and the remaining days"""

    # Iterates through each year until days remaining are less than a full year
    year = 1970
    while (leap_year(year) is True and days_remaining >= 366) or (leap_year(year) is False and days_remaining >= 365):
        if leap_year(year):
            days_remaining -= 366
            year += 1
        else:
            days_remaining -= 365
            year += 1

    return year, days_remaining


def find_month(days_remaining, year):
    """Determines the month of the new date and returns the month and the remaining days"""

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
    hex_str = '0'

    # Ensure the string has even number of characters, padding if needed
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str

    # Split the string into bytes 


    # Manually reorder the bytes if the endian type is little

    return hex_str
