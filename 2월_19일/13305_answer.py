n = int(input())

distance = list(map(int ,input().split()))

price = list(map(int , input().split()))

#최소 가격이 나올때 계속 갱신해주면 되는건가?
min_price  = price[0]
sum =0
for i in range(len(price)-1): #0 , 1 , 2 까지
    if price[i] <= min_price:
        min_price = price[i]
        sum += distance[i] * min_price
    else:
        sum+= min_price * distance[i]

print(sum)
