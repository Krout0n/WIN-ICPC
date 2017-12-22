d = { chr(i): 0 for i in range(96, 123) }
s = list(input())
for i in s:
    try:
        d[i.lower()] += 1
    except:
        continue
for i,j in d.items():
    print('{} : {}'.format(i,j))