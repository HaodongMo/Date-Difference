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

    # get dates in days from 1/1/1

    days1 = functions.dateToDays(day1, month1, year1)
    days2 = functions.dateToDays(day2, month2, year2)

    # calculate difference

    diff = days2 - days1
    
    # display as date1, date2, diff

    if diff >= 0:
        print(dates[0] + ", " + dates[1] + ", " + str(diff))
    else:
        print(dates[1] + ", " + dates[0] + ", " + str(diff * -1))