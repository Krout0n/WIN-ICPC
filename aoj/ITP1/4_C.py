while True:
    a, op, b = [i for i in input().split()]
    if op == '?':
        break
    print(int(eval(a+op+b)))