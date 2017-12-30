import math
def is_prime(x):
    if x < 2: return False
    if x == 2 or x == 3 or x == 5: return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False
    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0: return False

        prime += step
        step = 6 - step

    return True

for _ in range(int(input())):
    c = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if is_prime(i) and is_prime((i+1)/2):
            c += 1
    print(c)