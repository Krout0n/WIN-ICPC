import sys

s = input()
c = 1
d = {'2':0, '5':0}

for i in s:
    d[i] += 1

if d['2'] != d['5']:
    print(-1)
    sys.exit(0)

st = set()
st.add('')

while True:
    s = s.split('25')
    if not set(s).difference(set(st)):
        break
    s = ''.join(s)
    if not '25' in s and c < 2:
        print(-1)
        sys.exit(0)
    c += 1

print(c)
