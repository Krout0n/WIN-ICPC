m = int(input())
if m < 100:
    print('00')
elif 100 <= m <= 5000:
    m /= 100
    if m < 10:
        print(0,str(m)[0],sep='')
    else:
        print(int(m))
elif 6000 <= m <= 30000:
    m /= 1000
    print(int(m+50))
elif 35000 <= m <= 70000:
    m /= 1000
    print(int((m-30)/5 + 80))
else:
    print(89)
