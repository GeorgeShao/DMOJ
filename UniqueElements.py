# https://dmoj.ca/problem/set

num = int(input())

data_list = []

for i in range(num):
    data_list.append(int(input()))

data_set = set(data_list)

print(len(data_set))