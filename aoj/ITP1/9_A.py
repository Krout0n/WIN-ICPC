x = input()
c = 0
while True:
    s = input()
    if s == 'END_OF_TEXT':
        break
    s = s.split()
    for i in s:
        if x == i:
            c += 1

print(c)