import sys

d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

for s in sys.stdin:
    c = 0
    for i,j in enumerate(list(s)):
        if j == '\n':
            break
        try:
            if j == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                c -= 1
            elif j == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                c -= 10
            elif j == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                c -= 100
            else:
                c += d[j]
        except:
            c += d[j]
    print(c)
