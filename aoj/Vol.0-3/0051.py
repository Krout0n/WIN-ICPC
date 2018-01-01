
for _ in range(int(input())):
    i = input()
    max = int(''.join(sorted(list(i), reverse=True)))
    min = int(''.join(sorted(list(i))))
    print(max-min)