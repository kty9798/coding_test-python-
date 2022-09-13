from collections import deque


#n -> x개 m -> y개
m , n  = map(int , input().split())

#상하좌우
dx , dy = [-1 , 1 , 0 , 0] , [0 , 0 , -1 , 1]
queue = deque([])
graph = []
for _ in range(n):
    graph.append(list(map(int , input().split())))

res = 0

# 1만 골라 넣자

for row in range(n):
    for col in range(m):
        if graph[row][col] == 1:
            queue.append([row , col])


def bfs():
    while queue: #큐에서 1만 꺼내서

        x , y = queue.popleft()

        #시작 좌표에서 
        for i in range(4):
            nx= x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <n and 0 <= ny < m and graph[nx][ny] ==0:
                graph[nx][ny] = graph[x][y] +1 #1에서 1더하는것 
                queue.append([nx , ny])
                 

bfs()

for i in graph:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    
    res = max(res , max(i))

print(res -1)





# for x in range(m):
#     for y in range(n):
#         if graph[x][y] ==0:
#             continue
#         if graph[x][y] == -1:
#             continue
#         if graph[x][y] ==1:
#             dfs(x , y)

