import math

while True:
    i = int(input())
    if i == 0:
        break
    s = str(math.factorial(i))
    c = 0
    _c = 0
    for j in list(s):
        if j == '0':
            _c += 1
        else:
            _c = 0
        if c < _c:
            c = _c
    print(c)