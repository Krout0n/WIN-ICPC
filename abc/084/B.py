a,b = map(int, input().split())
s = input()
d = 0

for i in list(s):
    if i == '-':
        d += 1

try:
    map(int, s.split('-'))
    if len(s) == a + b + 1 and s[a] == '-' and d < 2:
        print('Yes')
    else:
        print('No')
except:
    print('No')