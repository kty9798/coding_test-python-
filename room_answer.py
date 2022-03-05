from importlib import import_module
import sys 


n = int(sys.stdin.readline())


time = [[0]* 2 for _ in range(n)]

for i in range(n):
    s , e = map(int , sys.stdin.readline().split())
    time[i][0] = s   #시작시간
    time[i][1] = e #끝시간

#sorting을 1번째로 끝 기준 두번째는 
time.sort(key = lambda x : (x[1] , x[0]))


#처음꺼를 1
result = 1
finish_time = time[0][1]

del time[0] #첫번쨰 지우기

print(time)
for i in time:
    #i[0] 은 시작시간
    if i[0] >= finish_time:
        result+=1
        finish_time = i[1]


print(result)

#1-4 5-7 8-11 12-14