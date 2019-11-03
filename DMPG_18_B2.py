import sys

n,m = sys.stdin.readline().split()
n = int(n)
m = int(m)

if n >= m:
    print(m-1)
elif n < m:
    print(n)