# https://dmoj.ca/problem/a4b1

num = int(input())
data = []

for i in range(num):
    data.append(int(input()))

data.sort()

for each in data:
    print(each)