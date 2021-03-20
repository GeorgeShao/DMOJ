# NOT WORKING (PARTIALLY WORKING)

from sys import stdin

m = int(stdin.readline().replace('\n', ''))
n = int(stdin.readline().replace('\n', ''))
k = int(stdin.readline().replace('\n', ''))

arr = [["B"]*n for i in range(m)]

for i in range(k):
    a, b = stdin.readline().replace('\n', '').split()
    b = int(b)
    if a == "C":
        for i in range(m): #column
            if arr[i][b-1] == "B":
                arr[i][b-1] = "G"
            else:
                arr[i][b-1] = "B"
    else:
        for i in range(n): #row
            if arr[b-1][i] == "B":
                arr[b-1][i] = "G"
            else:
                arr[b-1][i] = "B"

total = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == "G": #gold
            total += 1

print(total)