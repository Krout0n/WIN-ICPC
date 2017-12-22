s = []
while True:
    i = int(input())
    if not i:
        break
    s.append(i)

for i,j in enumerate(s):
    print('Case {}:{}'.format(i+1,j))
