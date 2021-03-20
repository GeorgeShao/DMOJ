# NOT WORKING (PARTIALLY WORKING)

from sys import stdin

n = int(stdin.readline().replace('\n', ''))

p = [] # initial position
w = [] # time it takes to walk 1 meter
d = [] # minimum hearing distance

for i in range(n):
    p1, w1, d1 = stdin.readline().replace('\n', '').split()
    p.append(int(p1))
    w.append(int(w1))
    d.append(int(d1))

min_pos = min(p)
max_pos = max(p)

times = []

for speaker_pos in range(min_pos, max_pos+1):
    time = 0
    for j in range(len(p)):
        if abs(p[j]-speaker_pos) <= d[j]:
            pass
        else:
            if p[j] <= speaker_pos:
                time += abs(p[j]-speaker_pos+d[j])*w[j]
            else:
                time += abs(p[j]-speaker_pos-d[j])*w[j]
        # print(speaker_pos, p[j], w[j], d[j], abs(p[j]-speaker_pos+d[j]), abs(p[j]-speaker_pos-d[j]), time)
    times.append(time)
    try:
        if times[-1] >= times[-2]:
            break
    except:
        pass
    # print(time)

print(min(times))