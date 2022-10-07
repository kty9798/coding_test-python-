import sys
input = sys.stdin.readline


N = int(input())

list=[]
#print(list(map(int, input().split())))
list.append(input().split())

for i in range(len(list[0])):
    list[0][i] = int(list[0][i])
print(list)
