s = 0
a = int(input()) + 1
b = int(input()) + 1
c = int(input()) + 1
x = int(input())
for i in range(a):
    for j in range(b):
        for k in range(c):
            if 500*i + 100*j + 50*k == x:
                s += 1
print(s)