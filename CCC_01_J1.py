import sys

h = int(sys.stdin.readline())

left = [" " for i in range(h)]
right = [" " for i in range(h)]
left[0] = "*"
right[-1] = "*"

for i in range(0, h-1, 2):
    print(*left, sep='', end='')
    print(*right, sep='')
    if left[-1] != "*":
        left[i+1] = "*"
        left[i+2] = "*"
        right[-i-2] = "*"
        right[-i-3] = "*"

for i in range(0, h, 2):
    print(*left, sep='', end='')
    print(*right, sep='')
    if left[1] != " ":
        left[-i-1] = " "
        left[-i-2] = " "
        right[i] = " "
        right[i+1] = " "