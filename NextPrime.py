# https://dmoj.ca/problem/bf3

import math

def isPrime(num):
    if num > 1:
        for i in range(2, math.floor(math.sqrt(num))):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

min = int(input())

while not isPrime(min):
    min += 1

print(min)