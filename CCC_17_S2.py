import sys

num_tides = int(sys.stdin.readline())
tides = list(map(int, sys.stdin.readline().split(' ')))

tides.sort()
organized_tides = list()

high_tide = True

if num_tides % 2 != 0:
    high_tide = False

for i in range(len(tides)):
    if high_tide:
        organized_tides.insert(0, tides[len(tides)-1])
        tides.pop()
        high_tide = False
    else:
        organized_tides.insert(0, tides[0])
        del tides[0]
        high_tide = True

for tide in organized_tides:
    print(str(tide) + " ", end="")