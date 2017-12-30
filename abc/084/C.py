import sys

N = int(input())
class Train():
    
    def __init__(self,c,start,frequecncy):
        self.c = c
        self.start = start
        self.frequecncy = frequecncy
    
    def solve(self,t):
        if t < self.start:
            return self.start + self.c
        else:
            c = 0
            while t < self.frequecncy + t:
                if (t - self.start) % self.frequecncy == 0:
                    return t
                t += 1


trains = []
for h,i in enumerate(sys.stdin):
    trains.append((Train(*map(int, i.split()))))

routes = []

for i in range(N-1):
    routes.append(range(i, N-1))

for i,j in enumerate(routes):
    t = 0
    if j == N - 1:
        print(0)
        break
    for k in j:
        print(k)
        t += trains[k].solve(t)
    print(t)