import math
r = 100000
for _ in range(int(input())):
    r *= 1.05
    r = math.ceil(r/10000)*10000
    print(r)