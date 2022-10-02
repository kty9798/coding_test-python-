import sys
from collections import deque
input = sys.stdin.readline

N= int(input())

# 나이트 움직임
#8번의 움직임
dx = [1, 2, 2, 1 ,-1 , -2 , -2 , -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(size , f_x , f_y , o_x , o_y):
    matrix = [[0] * size for _ in range(size)]
    visited = [[False]* size for _ in range(size)]


    
    queue = deque()
    queue.append((f_x , f_y))
    visited[f_x][f_y] = True
    while queue:
        e_x , e_y = queue.popleft()
        if e_x == o_x and e_y ==o_y:
            return matrix[e_x][e_y]
        for i in range(8):
            nx = e_x + dx[i]
            ny= e_y + dy[i]
            if nx >=0 and ny>=0 and nx <size and ny < size:
                if not visited[nx][ny]:
                    queue.append((nx , ny))
                    visited[nx][ny] = True
                    matrix[nx][ny] = matrix[e_x][e_y]+  1 

    

result = list()
for i in range(N):
    size= int(input())
    f_x , f_y = map(int , input().split()) #first location
    o_x , o_y = map(int , input().split()) 
    result.append(bfs(size ,f_x , f_y ,o_x , o_y))
    

for element in result:
    print(element)