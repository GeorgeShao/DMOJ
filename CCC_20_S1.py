import sys

num = int(sys.stdin.readline())

data = dict()

for i in range(num):
    input = sys.stdin.readline()
    data[int((input.split(' '))[0])] = int(input.split(' ')[1].replace('\n', ''))

times = sorted(data)

max_speed = 0

for i in range(len(times)-1):
    diff_dist = data[times[i+1]] - data[times[i]]
    diff_time = times[i+1] - times[i]
    speed = abs(diff_dist/diff_time)
    if speed > max_speed:
        max_speed = speed

print(max_speed)