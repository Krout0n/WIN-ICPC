s = input()
for i,j in enumerate(s):
    i += 1
    if i > 26:
        i %= 26
    if ord(j) - i < ord('A'):
        print(chr(ord('Z') + 1 - (ord('A')+i-ord(j))), end='')
    else:
        print(chr(ord(j) - i), end='')
print()