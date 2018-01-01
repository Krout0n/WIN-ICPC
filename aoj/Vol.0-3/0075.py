import sys

for i in sys.stdin:
    n, w, t = map(float, i.split(','))
    print(int(n)) if w/(t**2) >= 25 else print('', end='')
