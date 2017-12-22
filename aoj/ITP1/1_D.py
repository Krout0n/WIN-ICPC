S = int(input())
h = int(S/3600)
S %= 3600
m = int(S/60)
print('{}:{}:{}'.format(h,m,S%60))