d = {}
l = ''
s = input()
for i in s.split():
    if not i in d:
        d[i] = 0
    else:
        d[i] += 1
    if len(str(l)) < len(str(i)):
        l = i

print(sorted(d.items(), key=lambda x: x[1])[-1][0], l)
