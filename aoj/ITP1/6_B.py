d = {
    'S': set([i for i in range(1,14)]),
    'H': set([i for i in range(1,14)]),
    'C': set([i for i in range(1,14)]),
    'D': set([i for i in range(1,14)])
}
for _ in range(int(input())):
    m, n = [i for i in input().split()]
    d[m].remove(int(n))

for m in ['S','H','C','D']:
    for i in d[m]:
        print(m, i)