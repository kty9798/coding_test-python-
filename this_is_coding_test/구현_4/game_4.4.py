n , m= map(int , input().split())
x , y, direction = map(int , input().split())


matrix = [[0] *m for _ in range(n)] #방문 관련 정보 기입
matrix[x][y] = 1
array = list()
for i in range(n):
    array.append(list(map(int , input().split())))
#위아래 북동남서
dx = [-1 , 0 , 1, 0]
dy = [0 , 1 , 0 , -1]

#방향 전환 함수
def turn_left():
    #전역함수 지정
    global direction
    direction -= 1 
    if direction == -1: 
        direction = 3


#이제 돌면서 방문한 칸들을 확인하는 코드 
#variable 
count =1 
turn_time = 0
while True:
    turn_left() #방향이 변함
    nx = x + dx[direction]
    ny = y + dy[direction]
    if matrix[nx][ny] == 0 and array[nx][ny] ==0:
        matrix[nx][ny] =1
        count+=1 
        turn_time = 0
        x = nx
        y = ny
        continue
    #정면에 칸이 없거나 바다일때
    else:
        turn_time +=1

    if turn_time ==4: #다돌았을때
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] ==0:
            x  = nx
            y = ny
        else: #뒷면도 바다
            break

        turn_time = 0

print(count)




#자기 방문 count