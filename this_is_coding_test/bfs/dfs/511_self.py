from collections import deque
n  , m = map(int , input().split())

graph= list()
#상하좌우
dx = [-1 , 1 , 0 ,  0 ]
dy = [ 0 , 0 , -1 , 1 ]


for i in range(n):
    graph.append(list(map(int , input())))

#graph 채우기 

#핵심 bfs 내용 (최단거리)
def bfs(x , y):
    queue = deque()
    queue.append((x , y))


    while queue:
        x , y  = queue.popleft()
        for i in range(4):
            nx = x +  dx[i]
            ny = y + dy[i]

            if nx <0 or ny <0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] ==0:
                continue
            #이제 방문 안한 곳 있으면'

            if graph[nx][ny] ==1:
                graph[nx][ny]= graph[x][y] + 1
                queue.append((nx , ny))
    return graph[n-1][m-1]    

#n개 m개

print(bfs(0 , 0))