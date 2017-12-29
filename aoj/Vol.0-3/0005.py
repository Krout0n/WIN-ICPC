import sys

def gcd(x, y):
    if x % y != 0:
        return gcd(y, x % y)
    return y

for i in sys.stdin:
    x, y = map(int, i.split())
    g = gcd(x,y)
    print(g, int(x*y/g))