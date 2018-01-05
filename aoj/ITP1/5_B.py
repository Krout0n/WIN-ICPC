def build_line(width, i, h):
    s = ''
    if i == 0 or i == h-1:
        while len(s) < width:
                s += '#'
    else:
        s += '#'
        while len(s) < width - 1:
            s += '.'
        s += '#'
    return s

while True:
    h,w = [int(i) for i in input().split()]
    if not (h and w):
        break
    for i in range(h):
        print(build_line(w, i, h))
    print()
