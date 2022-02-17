n = int(input())

#16이면 11 6 1 
path = []
best = 0
while n==0:
    if len(path) ==0 and n%5 ==0:
        best = n//5
        break
    elif n <3:
        if len(path) ==0:
            best = -1
            break
        
    else:
        n -= 5
        path.append(n)
        best+=1

print(best)