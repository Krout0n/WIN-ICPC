import sys

# sys.setrecursionlimit(50000000)

coins = [1, 5, 10, 25, 50, 100]

def rec(n, idx):
    if idx == len(coins):
        idx = 0
    if n - coins[idx] == 0:
        return 1
    if n - coins[idx] < 0:
        return 0
    return rec(n-coins[idx], idx) + rec(n, idx+1)

print(rec(100, 0))