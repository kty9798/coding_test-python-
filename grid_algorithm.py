n = int(input())


best = 0
while n==0:
    if n%5 ==0:
        best = n/5
        break
    else:
        best = 1
        break

print(best)