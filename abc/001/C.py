import math

deg, dis = [float(i) for i in input().split()]
deg_list = ['N','NNE','NE','ENE','E' ,'ESE','SE','SSE','S' ,'SSW','SW','WSW','W' ,'WNW','NW','NNW']
wind_list = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6, math.inf]
d = 3487.5 - 3600
w = 0
d_i = 0
while d <= deg:
    d += 225
    d_i += 1
dis /= 60
dis = math.floor(dis)
for i,j in enumerate(wind_list):
    if i == 0 and dis < j:
        deg_list[d_i-1] = 'C'
    print(dis,j)
    if dis < j:
        w = i
        break
print(deg_list[d_i-1],w)