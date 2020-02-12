import sys

num_villages = int(sys.stdin.readline())
villages = list()

for i in range(num_villages):
    villages.append(int(sys.stdin.readline()))

villages.sort()

smallest_neighbourhood = 1000000001

for i in range(1, num_villages-1):
    left_range = (villages[i] - villages[i-1])/2
    right_range = (villages[i+1] - villages[i])/2
    if left_range + right_range < smallest_neighbourhood:
        smallest_neighbourhood = left_range + right_range

print(smallest_neighbourhood)