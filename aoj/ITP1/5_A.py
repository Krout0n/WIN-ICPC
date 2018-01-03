def build_line(width, i):
    s = ''
    while len(s) < width:
                s += '#'
    return s

while True:
    h,w = [int(i) for i in input().split()]
    if not (h and w):
        break
    for i in range(h):
        print(build_line(w, i))
    print()
