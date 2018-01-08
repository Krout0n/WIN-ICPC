y = [int(input()) for i in range(int(input()))]
y = sorted(set(y))
c = 1
max_c = 1
print(y)
for i,j in enumerate(y):
    try:
        if j < y[i+1]:
            c += 1
            if max_c < c:
                max_c = c
        else:
            c = 1
    except:
        pass
print(max_c)