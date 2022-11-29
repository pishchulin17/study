def get_days_of_month(month):
    if month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


data = input()
day = int(data[0] + data[1])
month = int(data[3] + data[4])
year = int(data[6] + data[7] + data[8] + data[9])
if day < 28 and get_days_of_month(month) == 28 and leap_year(year) is False:
    day += 1
elif day < 29 and get_days_of_month(month) == 28 and leap_year(year) is True:
    day += 1
elif day == 28 and get_days_of_month(month) == 28 and leap_year(year) is False:
    day = 1
    month += 1
elif day == 29 and get_days_of_month(month) == 28 and leap_year(year) is True:
    day = 1
    month += 1
elif day < 30 and get_days_of_month(month) == 30:
    day += 1
elif day == 30 and get_days_of_month(month) == 30:
    day = 1
    month += 1
elif day < 31 and get_days_of_month(month) == 31:
    day += 1
elif day == 31 and get_days_of_month(month) == 31 and (month != 12):
    day = 1
    month += 1
elif day == 31 and month == 12:
    year += 1
    day = 1
    month = 1

if month < 10 and day > 9 and year > 999:
    print(f'{day}.0{month}.{year}')
elif month < 10 and day < 10 and year > 999:
    print(f'0{day}.0{month}.{year}')
elif month >= 10 and day > 9 and year > 999:
    print(f'{day}.{month}.{year}')
elif month >= 10 and day < 10 and year > 999:
    print(f'0{day}.{month}.{year}')
elif month < 10 and day > 9 and year > 99:
    print(f'{day}.0{month}.0{year}')
elif month < 10 and day < 10 and year > 99:
    print(f'0{day}.0{month}.0{year}')
elif month >= 10 and day > 9 and year > 99:
    print(f'{day}.{month}.0{year}')
elif month >= 10 and day < 10 and year > 99:
    print(f'0{day}.{month}.0{year}')
elif month < 10 and day > 9 and year > 9:
    print(f'{day}.0{month}.00{year}')
elif month < 10 and day < 10 and year > 9:
    print(f'0{day}.0{month}.00{year}')
elif month >= 10 and day > 9 and year > 9:
    print(f'{day}.{month}.00{year}')
elif month >= 10 and day < 10 and year > 9:
    print(f'0{day}.{month}.00{year}')
elif month < 10 and day > 9 and year < 9:
    print(f'{day}.0{month}.000{year}')
elif month < 10 and day < 10 and year < 9:
    print(f'0{day}.0{month}.000{year}')
elif month >= 10 and day > 9 and year < 9:
    print(f'{day}.{month}.000{year}')
elif month >= 10 and day < 10 and year < 9:
    print(f'0{day}.{month}.000{year}')
