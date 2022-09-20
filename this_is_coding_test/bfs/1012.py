import sys 

from collections import deque

input= sys.stdin.readline

total_result= list()
T = int(input()) #T번 반복
def bfs(graph , x, y):
    cnt = 1
    dx , dy= [-1 , 1 , 0 , 0] ,[0 , 0 , -1 ,1]
    #상하좌우
    queue= deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x ,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 

            if nx <0 or ny <0 or nx >=N or ny>=M:
                continue

            if graph[nx][ny] ==1:
                graph[nx][ny] =0
                
                queue.append((nx , ny))             
                cnt+=1

    return cnt

for _ in range(T):
    M , N , K = map(int , input().split())
    #M은 가로길이 N은 세로길이 , 총 배추 위치 개수
    graph = [[0] *M  for _ in range(N)]

    for _ in range(K):
        a , b = map(int , input().split())
        graph[b][a] = 1
        #세로 가로

    #각 좌표만큼 반복
    result = list()
    for i in range(N):
        for j in range(M):
            if graph[i][j] ==1:
                result.append(bfs(graph , i , j))

    total_result.append(len(result))

for i in range(len(total_result)):
    print(total_result[i])
