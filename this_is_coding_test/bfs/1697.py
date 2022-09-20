N , K = map(int , input().split())
from collections import deque


#larger_one= max(N , K) #17

visited = [0] * 100001


a = (lambda x : x-1)
b = lambda x : x+1
c = lambda x : 2*x

action_list = [a, b, c]

def bfs(start , end):
    queue = deque()
    
    queue.append(start)
    visited[start] = 0

    while queue:
        x =queue.popleft()  

        if x == K:
            print(visited[x])
            break
        for nx in (x-1 , x+1 , 2*x):
            
            if 0 <= nx <= 100000 and visited[nx] ==0:
                visited[nx] = visited[x] +1
                queue.append(nx)
            
            
bfs(N , K)
# print(bfs(N , K))
# print(b(1))
# print(c(1))