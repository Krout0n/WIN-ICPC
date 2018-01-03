import sys

d = { chr(i): 0 for i in range(97, 123) }
s = [i for i in sys.stdin]
for i in s:
    i = list(i)
    for c in i:
        try: 
            d[c.lower()] += 1
        except:
            continue
for i,j in d.items():
    print('{} : {}'.format(i,j))