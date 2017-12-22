l = [
    [
        [
            0 for ___ in range(10)
        ] for __ in range(3)
    ] for _ in range(4)
]

for _ in range(int(input())):
    b,f,r,w = [int(i) for i in input().split()]
    l[b-1][f-1][r-1] += w

for a in l:
    for b in a:
        for i,c in enumerate(b):
            if i != 8:
                print(c, end=' ')
            else:
                print(c)
    print('####################')
