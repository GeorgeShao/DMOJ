import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

whole = a//b

if a == 0:
    print(0)
elif a % b == 0:
    print(whole)
else:
    if a//b == 0:
        if b%(a%b) != 0:
            factor = gcd(a, b)
            a = a//factor
            b = b//factor
        print(f"{a%b}/{b}")
    elif b%(a%b) == 0:
        a = a % b
        factor = gcd(a, b)
        a = a//factor
        b = b//factor
        print(f"{whole} {a%b}/{b}")