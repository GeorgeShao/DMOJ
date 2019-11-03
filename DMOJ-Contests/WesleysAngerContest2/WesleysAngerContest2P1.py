import sys

date = str(sys.stdin.readline())
arr = ["Sunday\n", "Monday\n", "Tuesday\n", "Wednesday\n", "Thursday\n", "Friday\n", "Saturday\n", "Sunday\n"]

date = arr[arr.index(date)+1].replace("\n", "")
print(date)