lines = int(input())

for i in range(lines):
  num, character = input().split()
  print(character * int(num))