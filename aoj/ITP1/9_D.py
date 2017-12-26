t = input()
for _ in range(int(input())):
    order = input().split()
    cmd = order[0]
    a, b = map(int,  order[1:3])
    if cmd == 'print':
        print(t[a:b+1])
    elif cmd == 'reverse':
        t = t[:a] + t[a:b+1][b::-1] + t[b+1:]
    else:
        c = order[3]
        t = t[:a] + c + t[b+1:]