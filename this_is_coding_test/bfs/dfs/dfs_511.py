from collections import deque

n , m = map(int , input().split()) #2개니까 split

graph = list()
for row in range(n):
    graph.append(list(map(int , input())))



#전체 n , m 다 돌면서 bfs 시행하면 된다
#상하좌우 정의
#상하좌우
#dx ,dy 쌍으로 0, 1,2 ,3 돌면서 적용하면 상하좌우 확인 가능 

dx = [-1 , 1 , 0 ,0]
dy = [0 , 0 , -1 , 1]


def bfs(x, y):
    queue = deque()
    
    queue.append((x, y))

    #큐가 빌때까지

    while queue:
        x , y = queue.popleft() #처음
        #현재 위치에서 4방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            #필터링 과정 == 벽면 혹은 벽일때 빼고
            if nx <0 or ny <0 or nx >=n or ny >= m: #이거 실수함
                continue

            if graph[nx][ny] ==0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] + 1 #최단거리 기록
                queue.append((nx , ny))

    return graph #가장 가쪽의 그래프 모양 반환 


print(bfs(0 , 0))
        


305070
234567
000008
14131211109
151413121110