n = int(input())

#16이면 11 6 1 
# path = []
best = 0
# while n>0:
#     if len(path) ==0 and n%5 ==0:
#         best = n//5
#         break
#     elif n%5==0:
#         best += n//5
#     elif n <5:
#         if len(path) ==0:
#             best = -1
#             break
#         if path[-1] %3 ==0:
#             best +=1
#             break
#         best = -1
#         break                   
#     else:
#         n -= 5
#         path.append(n)
#         print(path)
#         best+=1

# print(best)


while n>=0:
    if n%5==0:
        best += n//5
        print(best)
        break
    n-= 3
    best +=1

else:
    print(-1)