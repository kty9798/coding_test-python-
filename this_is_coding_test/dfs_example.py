def dfs(graph , v , visited):
    visited[v] = True
    print(v , end = ' ')

    for i in  graph[v]:
        if not visited[i]:
            dfs(graph , i  , visited)


# 0 , 1 ,2 ,3 ,5 인접한 것
# 
# 
# 들끼리 나타냄

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
    dfs(graph , 1 , visited)

#들어오는 입력 형태 인접 매트릭스 아니면 인접 시스트