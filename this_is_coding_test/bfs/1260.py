from collections import deque 

import sys


input = sys.stdin.readline
N , M , F = map(int , input().split())
visited_d = [0] * (N+1)


graph = [[] for _ in range(N+1)]

visited = [[0] for _ in range(N+1)]
result = []

for _ in range(M):
    a , b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)


for element in graph:
    element.sort()


def dfs(x):
    #firsted[] = 
    visited_d[x] = 1
    result.append(x)
    for i in graph[x]:
        if visited_d[i] ==0:
            dfs(i)
    




def bfs(first):
    visited_b= [0] * (N+1)
    result  = list()
    queue = deque()
    queue.append(first)
    result.append(first)
    visited_b[first] = 1

    while queue:
        element = queue.popleft()


        for i in graph[element]:
            if visited_b[i] == 0:
                visited_b[i] = 1
                result.append(i)
                queue.append(i)

    return result









dfs(F)
# print("dfs" , result)
for i in result:
    print(i , end = " ")
print("")
bfs_result =bfs(F)
for j in bfs_result:
    print(j , end= " ")


