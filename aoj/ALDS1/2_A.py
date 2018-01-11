input()
A = [int(i) for i in input().split()]
c = 0
def bubble_sort(A):
    global c
    flag = True
    while flag:
        flag = False
        for i in range(len(A)-1, 0, -1):
            if A[i] < A[i -1]:
                A[i], A[i -1] = A[i -1], A[i]
                c += 1
                flag = True
bubble_sort(A)
print(*A)
print(c)