n , m = map(int , input().split())

#상하좌우
dx = [-1 , 1 , 0 , 0]
dy = [0 , 0 , -1 , 1]
graph = []
for _ in range(m):
    graph.append(list(map(int , input().split())))


print(graph)


def bfs(x, y):
    pass

for x in range(m):
    for y in range(n):
        if graph[x][y] ==0:
            continue
        if graph[x][y] == -1:
            continue
        if graph[x][y] ==1:
            dfs(x , y)
