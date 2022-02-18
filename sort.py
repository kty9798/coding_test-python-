#test
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))


sorted_a = sorted(a)

for i in sorted_a:
    print(i , end="\n")