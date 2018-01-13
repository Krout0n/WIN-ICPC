x = input().split()
s = []
for i in x:
    try:
        i = int(i)
        s.append(i)
    except:
        s.append(eval('{b}{ope}{a}'.format(a=s.pop(), ope=i, b=s.pop())))
print(s[0])