n = int(input())
#lstrip rstrip 개행 없애는것

list = []

b = 0

for i in range(n):
    b = int(input())
    list.append(b)

list = sorted(list)
#print(sum(list)//5)
mean = round(sum(list)/n)
#index가 0 1 2 3 4 즉 len-1/2
# 0 1-1/2
median = list[(len(list)-1)/2]

print(mean)
print(median)
#print(freq)
#print(range)

#print(list)