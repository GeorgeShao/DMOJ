# NOT WORKING

import sys

computers = int(sys.stdin.readline())
scores = {}
perm = {}

if computers == 0:
    sys.exit()

for i in range(computers):
    name, r, s, d = sys.stdin.readline().split()
    name = str(name)
    r = int(r)
    s = int(s)
    d = int(d)
    score = 2*r + 3*s + d
    scores[name] = score
    perm[name] = score

if computers == 1:
    print((max(scores.items(), key=lambda x: x[1]))[0])
    sys.exit()

first_place = (max(scores.items(), key=lambda x: x[1]))[0]

del scores[first_place]

second_place = (max(scores.items(), key=lambda x: x[1]))[0]

if perm[first_place] == perm[second_place]:
    temp = [first_place, second_place]
    temp.sort()
    print(temp[0])
    print(temp[1])
else:
    print(first_place)
    print(second_place)