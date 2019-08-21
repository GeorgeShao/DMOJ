import sys

input = sys.stdin.readline

num_of_intervals, destination = input().split()

intervals = list(map(int, input().split()))

results = []

destination = abs(int(destination))

for i in range(len(intervals)):
    if (int(destination) % int(intervals[i])) == 0:
        results.append(int(destination)/int(intervals[i]))
    else:
        results.append(100000)

results.sort()
if results[0] != 100000:
    print(int(results[0]))
else:
    print("This is not the best time for a trip.")