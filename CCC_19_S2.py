import sys
import math

def is_prime(num: int):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def find_case(num: int, i: int):
    if is_prime(num-i):
        if is_prime(num+i):
            print(str(num-i), str(num+i))
        else:
            find_case(num, i+1)
    else:
        find_case(num, i+1)

num_cases = int(sys.stdin.readline())
cases = []

for i in range(num_cases):
    num = int(sys.stdin.readline())
    find_case(num, 0)