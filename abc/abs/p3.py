c = 0
input()
a = [int(i) for i in input().split()]
while not list(filter(lambda x:x % 2 == 1, a)):
    c += 1
    a = list(map(lambda x: x / 2, a))
print(c)