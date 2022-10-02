import sys
from collections import deque

input = sys.stdin.readline
N , M = map(int , input().split())
#사다리 수 시작 끝 
#뱀의 수 시작 끝을 설명할수 있는 자료구조'

branch = dict()
snake = dict()
result_count = [0] * 101
visited = [False]* 101

for _ in range(N):
    a , b=  map(int , input().split())
    branch[a] = b

for _ in range(M):
    a , b=  map(int , input().split())
    snake[a] = b

def bfs():
    options = [1,2,3,4,5,6]    
    queue = deque()
    queue.append(1)
    
#사다리는 올라가고 뱀은 내려가고 방문숫자는 
    #1일때
    while queue:
        now_point =queue.popleft()
        
        if now_point == 100:
            return result_count[now_point]

        #next step은 2부터 7까지
        #1이다 그런데 1+1 ~6
        for step in options:
            next_step = now_point + step
            
            if 0<next_step<=100 and not visited[next_step]:
                #사다리
                if next_step in branch.keys():
                    next_step = branch[next_step]
                    #queue 에 들어간다는게 방문했다는 방증
                if next_step in snake.keys():
                    #next step이 12다 
                    #12의 카운트는 7의 방문+1
                    next_step = snake[next_step]
                
                if not visited[next_step]:
                    queue.append(next_step)
                    visited[next_step] = True
                    result_count[next_step] = result_count[now_point] + 1
                 

        #사다리에 걸렸을때
        #뱀에 걸렸을떄
#1 7 (12-98) 100
result = bfs()

print(result)
