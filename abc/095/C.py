a,b,c,x,y = map(int, input().split())
c *= 2
mi = a*x + b*y

for i in range(x+1):
    v = x-i
    s = a*i + b*(y-v) + c*v
    if y <= v:
        s = a*i + c*v
    if s < mi:
        mi = s

for i in range(y+1):
    v = y-i
    s = a*(x-v) + b*i + c*v
    if x <= v:
        s = b*y + c*v
    if s < mi:
        print('h', a*(x-v) + b*i + c*v)
        mi = s

if c*max((x,y)) < mi:
    mi = c*max((x,y))

print(mi)
