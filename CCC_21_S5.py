# NOT WORKING AT ALL

from sys import stdin

n, m= stdin.readline().replace('\n', '').split()
n = int(n)
m = int(m)

rule_a = []
rule_b = []
rule_c = []

for i in range(m):
    a, b, c = stdin.readline().replace('\n', '').split()
    rule_a.append(int(a))
    rule_b.append(int(b))
    rule_c.append(int(c))

multiplier = 1

answer = []

for i in range(n):
    multiplier = 1
    for j in range(m):
        if i in range(rule_a[i]-1, rule_b[i]):
            multiplier *= rule_c[i]
    try:
        answer.append(answer[-1]*multiplier)
    except:
        answer.append(multiplier)

print(answer)