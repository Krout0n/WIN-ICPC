s = input()
words = ['dream', 'dreamer', 'erase', 'eraser']
d = set()
def rec(i, b, c):
    p = b + words[i]
    key = '{}{}->{}{}'.format(words[i],c, s[c:c+len(words[i])],c+len(words[i]))
    if key in d:
        return False
    if words[i] != s[c:c+len(words[i])]:
        d.add(key)
        return rec((i+1)%4, b, c) or rec((i+2)%4, b, c) or rec((i+3)%4, b, c)
    if p == s:
        return True
    return rec((i+1)%4, p, c+len(words[i])) or rec((i+1)%4, b, c)

print('YES') if rec(0, '', 0) else print('NO')
