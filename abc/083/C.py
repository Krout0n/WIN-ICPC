def rec(result, i, dest, step):
    print('i > dest: ', i, dest)
    if i > dest:
        return result
    if i % result[-1] == 0:
        result.append(i)
        rec(result, i+result[-1], dest, result[-1])
    else:
        rec(result, i+step, dest, result[-1])
        
x, y = [int(i) for i in input().split()]
l = [x]
ans = rec(l, 2*x, y, x)
print(len(l))
