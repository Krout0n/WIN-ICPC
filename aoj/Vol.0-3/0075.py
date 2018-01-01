# 1001,50.0,1.60 
# 1002,60.0,1.70 
# 1003,70.0,1.80 
# 1004,80.0,1.70 
# 1005,90.0,1.60 
import sys

for i in sys.stdin:
    n, w, t = map(float, i.split(','))
    print(int(n)) if w/(t**2) >= 25 else print('', end='')
