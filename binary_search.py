import sys

n = int(input())


list_n = list(map(int , sys.stdin.readline().split()))
list_n =sorted(list_n)

m = int(sys.stdin.readline())

list_m = list(map(int , sys.stdin.readline().split()))
#list_m = sorted(list_m)

#print(list_n)
#print(list_m)


result = []
for i in range(len(list_m)):
    if list_m[i] in list_n:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)
