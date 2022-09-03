#기본 가정 a부터 h
#y는 1- 8

input= input()
result = 0

x_locate_dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7,  "h" : 8}
#혹은 아스키 코드로 변환
x_new = int((ord(input[0]))) - int(ord("a")) + 1
        #str 타입 97

x_locate = x_locate_dict[input[0]]
y_locate = int(input[1])

steps = [[2, 1] , [-2, -1] , [-2, 1], [2, -1] ,[1,2] , [-1,-2],[-1,2],[1,-2]]
#해당 1,1 부터 8,8까지에서 하나라도 0이 되면 안됨
for step in steps:
    
    after_x = x_locate + step[0]
    after_y = y_locate + step[1]

    if after_x >0 and after_x <=8 and after_y >0 and after_y <=8:
        print(after_x , after_y)
        result+=1


print(result)
#해당 좌표를 2차원 좌표로 변환해야됨 