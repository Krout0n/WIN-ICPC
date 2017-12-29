def gcd(x, y):
    if x % y != 0:
        return gcd(y, x % y)
    return y

print(gcd(*[int(i) for i in input().split()]))