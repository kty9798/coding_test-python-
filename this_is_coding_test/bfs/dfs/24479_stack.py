import sys

input = sys.stdin.readline
N , M , R = map(int , input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a , b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)

for element in graph:
    element.sort(reverse = True) #거꾸로 해야지 마지막 스택에 가장 낮은것이 먼저 뽑힘

def dfs(start):
    stack = [start] #stack 은 파이썬 list 로 구현 
    visited = [-1] * (N+1)
    result = [0] * (N+1)
    cnt = 1
    
    while stack:
        #1 없어짐
        cnt_node = stack.pop()
        if visited[cnt_node] == 1:
            continue
        
        visited[cnt_node] = 1 #방문 확인 
        result[cnt_node] = cnt
        cnt +=1
        #인접 노드 스택에 넣어줌 
        for near_node in graph[cnt_node]:
            if visited[near_node] == -1:
                stack.append(near_node)


    return result

results = dfs(R)

for i in range(1 , len(results)):
    print(results[i])

