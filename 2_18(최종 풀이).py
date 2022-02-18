n = int(input())
list =[]
result = []
for i in range(n):
    list.append(int(input()))

list =sorted(list)    
#sorting
#20 20

#32 25*2 20*3 18*4 72

for i in range(1, n+1):
    result.append(list[-i] * i)
    
print(max(result))