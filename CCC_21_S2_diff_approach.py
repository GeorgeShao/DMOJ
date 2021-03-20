# NOT WORKING (PARTIALLY WORKING)

from sys import stdin

m = int(stdin.readline().replace('\n', ''))
n = int(stdin.readline().replace('\n', ''))
k = int(stdin.readline().replace('\n', ''))

com_a = []
com_b = []

for i in range(k):
    a, b = stdin.readline().replace('\n', '').split()
    b = int(b)-1
    com_a.append(a)
    com_b.append(b)

total = 0

for i in range(m):
    for j in range(n):
        status = False
        indices = [z for z, x in enumerate(com_b) if x == i] #row
        for ind in indices:
            if com_a[ind] == "R":
                status = not status
        indices = [z for z, x in enumerate(com_b) if x == j] #col
        for ind in indices:
            if com_a[ind] == "C":
                status = not status
        if status:
            total += 1

print(total)