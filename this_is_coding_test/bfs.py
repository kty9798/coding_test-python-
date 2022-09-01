#queue를 사용하기 위해서
from collections import deque





def bfs(graph , start , visited):
    #생성 
    queue = deque([start])
    #방문 처리
    visited[start] = True
    while queue:
        v = queue.popleft() #v는 방문
        print(v , end=  " ")
        #queue.append(graph[v]) #[이러면 리스트 형태로 들어가게 됨
        for ad in graph[v]:
            if visited[ad] != True:
                queue.append(ad)
                visited[ad] = True




graph = [[],
         [2,3],
         [1, 7],
         [1,4  , 5],
         [3,5] ,
         [3,4] ,
         [7],
         [2 , 6, 8] ,
         [1, 7]]

visited = [False] * 9 #0 -> 9 

if __name__ == "__main__":
    # print("bfs result is \n")
    # bfs(graph , 1 , visited)
    print(int(1e9))