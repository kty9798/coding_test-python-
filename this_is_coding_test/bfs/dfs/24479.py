import sys
input = sys.stdin.readline # sys.stdin.readline
sys.setrecursionlimit(100**9) #제귀 횟수 제한 


N , M  , first = map(int , input().split())

graph = [[] for _ in range(N+1)]  #
path = []

result = [0] * (N+1)
visited = [-1] * (N+1)  #default 는 -1

for _ in range(M):
    a , b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)
    #둘 다 넣어줌 

for i in range(1, len(graph)):
    graph[i].sort()



def dfs(start):
    visited[start] =1
    path.append(start)
    #print(start , " ")
    
    for i in  graph[start]:
        if visited[i] == -1:
            dfs(i)



dfs(first)
#print(visited)

#4번만큼 path에 있는 만큼 result 리스트에 넣어줌
for idx , node in zip(range(1, len(path)+1) , path):
    result[node] = idx #순서 

for i in result[1:]:
    print(i)

# 예상
# 0[]
# 1[4 , 2]
# 2[3 , 4]
# 3[4]
# 4[]
# 5[]