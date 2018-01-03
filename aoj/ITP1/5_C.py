def build_line(width, i):
    s = ''
    if i % 2 == 0:
        while len(s) < width:
            if len(s) % 2 == 0:
                s += '#'
            else:
                s += '.'
    else:
        while len(s) < width:
            if len(s) % 2 == 0:
                s += '.'
            else:
                s += '#'
    return s

while True:
    h,w = [int(i) for i in input().split()]
    if not (h and w):
        break
    for i in range(h):
        print(build_line(w, i))
    print()
