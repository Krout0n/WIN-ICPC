def insersion_sort(a):
    print(*a)
    n = len(a)
    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = v
        print(*a)

input()
insersion_sort([int(i) for i in input().split()])