import sys

people = int(input())

for i in range(people):

    year, month, day = sys.stdin.readline().split()
    year = int(year)
    month = int(month)
    day = int(day)

    eligible = False

    if year == 2007 - 18:
        if month == 2:
            if day <= 27:
                eligible = True
        elif month < 2:
            eligible = True
    elif year < 2007 - 18:
        eligible = True

    if eligible:
        print("Yes")
    else:
        print("No")