import sys
sys.setrecursionlimit(10000)

input()
a = [int(i) for i in input().split()]

def solve(i, m):
    if m == 0:
        return True
    if i >= len(a):
        return False
    return solve(i+1, m) or solve(i+1, m - a[i]) # m - a[i] でその数字を使ったかどうか判定する

input()
for i in input().split():
    print('yes') if solve(0, int(i)) else print('no')
