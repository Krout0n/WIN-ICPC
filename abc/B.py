a = [i**2 for i in range(4, 334)]
b,c = input().split()
print(int(b+c) in a and 'Yes' or 'No')
