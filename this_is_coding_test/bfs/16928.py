import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int , input().split())

node = [[0] for i in range(101)]


for _ in range(N+M):
    a , b= map(int , input().split())
    node[a][0] = b

print(node)

#최소 몇번

def bfs(node , start):
    cnt = 0
    queue = deque()
    queue.append(start)
#element 1일떄 
#2,3, 4 5 6 7 다 들어가고 cnt 1증가하고
#2일때 
#3,4,5,6,7,8들어가고 cnt 1증가하고
#3일때 456789
    while queue:
        element = queue.popleft()
        for i in (1,2,3,4,5,6): #1
            next = element+i
            if next ==100:
                return cnt
            elif node[next] ==0:
                queue.append(next)
            else:
                queue.append(node[next])
        cnt+=1

