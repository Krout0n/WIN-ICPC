c = 0
def is_prime(n):
    for i in range(2, int(n**1/2)+1):
        if not(n % i):
            return False
    return True
for _ in range(int(input())):
    if is_prime(int(input())):
        c += 1
print(c)
