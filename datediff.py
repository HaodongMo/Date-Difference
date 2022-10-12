# Program for reading in two dates, then calculating the difference in days
# Date format is DD MM YYYY

import functions

f = open("test.txt", "r")
txt = f.read()

for line in txt.splitlines():
    dates = line.split(",")

    dates[0] = dates[0].strip()
    dates[1] = dates[1].strip()

    date1 = dates[0].split(" ")
    date2 = dates[1].split(" ")

    day1 = 0
    month1 = 0
    year1 = 0

    day2 = 0
    month2 = 0
    year2 = 0

    try:
        day1 = int(date1[0])
        month1 = int(date1[1])
        year1 = int(date1[2])

        day2 = int(date2[0])
        month2 = int(date2[1])
        year2 = int(date2[2])
    except:
        print("Invalid date format")

    if year1 > year2:
        raise Exception("Date 1 is after date 2")

    diff_years = year2 - year1

    if month1 > month2 and year1 == year2:
        raise Exception("Date 1 is after date 2")

    diff_months = month2 - month1

    if day1 > day2 and month1 == month2 and year1 == year2:
        raise Exception("Date 1 is after date 2")

    diff_days = day2 - day1

    if diff_years > 0:
        for i in range(year1, year2):
            if functions.isLeapYear(i):
                diff_days += 366
            else:
                diff_days += 365

    if diff_months > 0:
        for i in range(month1, month2):
            diff_days += functions.daysInMonth(i, year1)

    print(line, ", ", diff_days, sep="")