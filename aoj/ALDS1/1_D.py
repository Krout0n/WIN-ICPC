R = [int(input()) for _ in range(int(input()))]
ax = -2000000000000
mn = R[0]
for h,i in enumerate(R):
    if h == 0:
        continue
    ax = max([ax, i - mn])
    mn = min([mn, i])
print(ax)