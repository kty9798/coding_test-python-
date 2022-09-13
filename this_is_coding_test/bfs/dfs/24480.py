import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8) #limit 를 10^8승까지 많이 줘야됨



N , M , first= map(int , input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 1
# ans = [0] * (N+1)

for _ in range(M): #간선의 수 만큼
    a , b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)



def dfs(x):
    global count
    visited[x] = count
    #ans[x] = count
    graph[x].sort(reverse = True)

    for near_node in graph[x]:
        if visited[near_node] ==0:
            count+=1
            dfs(near_node)


dfs(first)

for i in range(1 , len(visited)):
    print(visited[i])