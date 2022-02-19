#연결된다
#1 3 6 9 13

n = int(input())
list = []
a = input().split()
for i in range(len(a)):
    list.append(int(a[i]))

list= sorted(list)
for i in range(1 , len(list)):
    list[i] += list[i-1]

print(sum(list))
#결과 32가 나와야됨