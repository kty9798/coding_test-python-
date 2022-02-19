#m , n = int(input().split(" "))
#map을 쓰던데...
#split 으로 쪼개고(defalut 가 문자열) 원론적 방법
'''
a  , b = input().split()
a ,b = int(a) , int(b)

print( a+ b)
'''

n , total=map(int, input().split())  
list =[]
count = 0
a = 0

for i in range(n):
    a= int(input())
    if a <= total:
        list.append(a)
    
#실수1.  같은 금액으로 딱 떨어지는 것도 넣어야 하니 list에 넣어줄때 작거나 같다로 넣어줘야됨



#700원이면 500원빼면 200원
#100원으로 나누면 200-> 100 count 2 
#100 -> 0 count 3 
#0이고 count는 3인데 루프 돌지만 다 잔돈보다 작으니 
while total >0:
    if total >= list[-1]:
        total = total - list[-1]
        count+=1
    elif len(list)==0:
        break #작거나 같을때
    else:    
        list.pop()
 
print(count)


#