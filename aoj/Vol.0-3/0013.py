import sys

s = []

for i in map(int, sys.stdin):
    # print(i, s)
    if i:
        s.insert(len(s), i)
    else:
        print(s.pop())
