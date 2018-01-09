x = int(input())
print(int(sum([float(i)/float(x)*10000 for i in range(1,x+1)])))