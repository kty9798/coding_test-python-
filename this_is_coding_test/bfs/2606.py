import sys

from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a , b = map(int , input().split()) 
    graph[a].append(b)
    graph[b].append(a)




cnt  = 0

def bfs(graph , start):
    global cnt
    visited = [-1] * (N+1)
    
    
    visited[start] = 1
    queue = deque() # 
    queue.append(start)

    while queue:
        #2번째
        start_node = queue.popleft() #처음 나가는 것들 
        
        cnt +=1
        # visited[start_node] = 1
                                #2 4 
        for near_node in graph[start_node]:
            if visited[near_node] == -1:
                visited[near_node] = 1
                queue.append(near_node)

    return cnt - 1


print(bfs(graph , 1))