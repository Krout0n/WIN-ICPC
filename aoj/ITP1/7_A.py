while True:
    m, f, r = [int(i) for i in input().split()]
    if m == f == r == -1:
        break
    s = m + f
    if m == -1 or f == -1:
        print('F')
        continue
    if s >= 80:
        rank = 'A'
    elif 65 <= s < 80:
        rank = 'B'
    elif 50 <= s < 65 or (30 <= s < 50 and r >= 50):
        rank = 'C'
    elif 30 <= s < 50:
        rank = 'D'
    elif s < 30:
        rank = 'F'
    print(rank)
    