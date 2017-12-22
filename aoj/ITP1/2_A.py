a, b = [int(i) for i in input().split()]
if a < b:
    op = '<'
elif a > b:
    op = '>'
else:
    op = '=='
print('a {} b'.format(op))