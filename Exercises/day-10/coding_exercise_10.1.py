def is_leap(year):
    """
    Check if a given year is a
    leap year.
    :param year:
    :return: True or False
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """
    Returns the number of days in
    a given month within a given year.
    :param year:
    :param month:
    :return: days
    """
    if month > 12 or month < 1:
        return 'Invalid month'
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] += 1
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)