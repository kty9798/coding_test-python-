n = int(input())
price = []
require = []
first_case , second_case = 0 , 0
a = input().split()
b = input().split()
for i in range(n-1):
    price.append(int(a[i]))
    require.append(int(b[i]))
    first_case += (price[i] * require[i])


total_price = sum(price)
#max min의 index를 찾기
min_require =min(require) 
min_index = require.index(min_require)

#remain
remain = 0
for i in range(min_index):
    second_case += (price[i] * require[i])

for i in range(min_index , len(price)):
    remain+= price[i]
second_case += remain * min_require


#second_case += require[min_index] *  

#1번 케이스 그냥 인덱스별로 곱하기
#print("first case is " , first_case)
print(min([first_case , second_case]))
#print("second case price is  "  , second_case)



#a>=2 b>=3 c>=1이상 = 6
#경우의 수가 필요 전에서 가격 최소에 몰고 그전까지 채우고
#아니면 각각까지 곱
#ex) 2가 젤 작으니까 그위치 전까지
#최소 곱 , 그이후는 나머지
#필요한거는 토탈 그리고 가격 최소 인덱스 그리고 

