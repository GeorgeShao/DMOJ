import sys

days = int(sys.stdin.readline())

runs1 = list(sys.stdin.readline().split(" "))
runs2 = list(sys.stdin.readline().split(" "))

sum1 = 0
sum2 = 0

max_equal_runs = 0

for i in range(days):
    sum1 += int(runs1[i])
    sum2 += int(runs2[i])
    if sum1 == sum2:
        max_equal_runs = i+1

print(max_equal_runs)