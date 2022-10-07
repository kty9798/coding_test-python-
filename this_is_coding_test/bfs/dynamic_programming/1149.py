import sys

input = sys.stdin.readline

N = int(input())

color = list()
for _ in range(N):
    a,b,c = map(int , input().split())

    color.append([a,b,c])


for i in range(1 , N): 
    for j in range(3):
        #j가 0일때 1 ,2
        if j==0:
            color[i][j] = color[i][j] + min(color[i-1][j+1] , color[i-1][j+2])        
        if j==1:
            color[i][j] = color[i][j] + min(color[i-1][j+1] , color[i-1][0]) 
        if j==2:
            color[i][j] = color[i][j] + min(color[i-1][1] , color[i-1][0])


print(min(color[N-1]))