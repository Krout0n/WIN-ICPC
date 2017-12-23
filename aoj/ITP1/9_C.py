n1 = n2 = 0
for _ in range(int(input())):
    a, b = input().split()
    if a == b:
        n1 += 1
        n2 += 1
        continue
    if sorted((a,b))[0] == b:
        n1 += 3
    else:
        n2 += 3

print(n1, n2)
