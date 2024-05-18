def conv_num(num_str):
    pass


def my_datetime(num_sec):
    """Takes an integer value that represents the number of seconds
        since the epoch (01/01/1970) and returns the date as a string
        """

    # Calculates the number of days
    year_days_remaining = (num_sec/86400)

    return num_sec


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


def conv_endian(num, endian='big'):
    pass
