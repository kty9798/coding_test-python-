from collections import deque


N= int(input())
graph = []
#visited = [[0] *(N) for _ in range(N)]

for i in range(N): #0 - 6
    graph.append(list(map(int, input())))




def bfs(graph , x, y):  
    dx , dy = [-1, 1, 0 ,0] , [0 , 0 ,-1 , 1] 
    queue = deque()
    queue.append((x , y))
    #0으로 바꿔서 다시 안하게
    graph[x][y] = 0 
    cnt =1
    while queue:
        x, y=queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or ny<0 or nx>=N or ny>= N:
                continue

            if graph[nx][ny] ==1:
                graph[nx][ny] =0
                queue.append((nx , ny))
                cnt+=1

    return cnt

result = list()
for i in range(N): #7 , 7 
    for j in range(N):
        
        if graph[i][j] == 1:
            result.append(bfs(graph , i ,j))
print(len(result))
result.sort()
for element in result:
    print(element)

#bfs로하던 dfs로 하던 탐색을 끝까지 하면되는건가