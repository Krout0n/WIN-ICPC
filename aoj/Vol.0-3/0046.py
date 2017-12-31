import sys
import math
maxv = 0
minv = math.inf
for i in map(float, sys.stdin):
    maxv = max([i, maxv])
    minv = min([i, minv])
print(maxv - minv)
