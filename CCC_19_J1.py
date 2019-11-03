Ascore3 = int(input()) * 3
Ascore2 = int(input()) * 2
Ascore1 = int(input())
Bscore3 = int(input()) * 3
Bscore2 = int(input()) * 2
Bscore1 = int(input())

if Ascore3 + Ascore2 + Ascore1 > Bscore3 + Bscore2 + Bscore1:
  print("A")
elif Ascore3 + Ascore2 + Ascore1 < Bscore3 + Bscore2 + Bscore1:
  print("B")
else:
  print("T")