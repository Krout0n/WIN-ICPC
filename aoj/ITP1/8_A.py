s = input()
end = ''
for h,i in enumerate(list(s)):
    if ord(i) in range(ord('A'), ord('Z')):
        print(i.lower(), end=end)
    elif ord(i) in range(ord('a'), ord('z') + 1):
        print(i.upper(), end=end)
    else:
        print(i, end=end)
print()