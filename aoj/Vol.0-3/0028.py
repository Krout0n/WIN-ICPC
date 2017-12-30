import sys

d = {i:0 for i in range(1,101)}
for i in map(int, sys.stdin):
    d[i] += 1
s = sorted(d.items(), key=lambda x: x[1], reverse=True)
m = s[0][1]
for i in s:
    if i[1] < m:
        break
    print(i[0])