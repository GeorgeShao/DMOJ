import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif a + b + c == 180 and a != b and b != c and c != a:
    print("Scalene")
elif a + b + c == 180 and a == b:
    print("Isosceles")
elif a + b + c == 180 and b == c:
    print("Isosceles")
elif a + b + c == 180 and c == a:
    print("Isosceles")
elif a + b + c != 180:
    print("Error")