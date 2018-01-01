import sys

s = 0
n = 0
c = 0
for i in sys.stdin:
    a,b = map(int, i.split(','))
    s += a * b
    n += b
    c += 1
print(s, round(n/c), sep='\n')
