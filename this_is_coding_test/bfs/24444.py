import sys
from collections import deque

input = sys.stdin.readline
N , M , R = map(int , input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a , b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)

for elements in graph:
    elements.sort(reverse = True)

cnt  = 1

def bfs(graph , start):
    global cnt
    visited = [-1] * (N+1)
    result = [0] * (N+1)
    
    visited[start] = 1
    queue = deque() # 
    queue.append(start)

    while queue:
        #2번째
        start_node = queue.popleft() #처음 나가는 것들 
        result[start_node] = cnt 
        cnt +=1
        # visited[start_node] = 1
                                #2 4 
        for near_node in graph[start_node]:
            if visited[near_node] == -1:
                visited[near_node] = 1
                queue.append(near_node)

    return result
results = bfs(graph , R)

for i in range(1 , len(results)):
    print(results[i])
        #2번의 인접 노드 1, 2,3  4번  #1번 X , 2번