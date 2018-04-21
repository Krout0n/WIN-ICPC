a, n = map(int, input().split())
for z in range(a+1):
    for y in range(a-z+1):
        x = a - z - y
        if 10000*x + 5000*y + 1000*z == n:
            print(x,y,z)
            exit()
print("-1 -1 -1")
