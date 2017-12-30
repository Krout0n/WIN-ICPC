import itertools, sys

d = [0 for i in range(51)]
print(d)
[a+b+c+d for a in range(10) for b in range(10) for c in range(10) for d in range(10)]
print(d)