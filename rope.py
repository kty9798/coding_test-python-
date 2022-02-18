#n = int(input())
list =[]
# for i in range(n):
#     list.append(int(input()))

example = ['1','2','3','4']

#4! 24 4c4 4c3 4c2 4c1 1+ 4+6 + 4
#1,2,3,4, 12 13 14 24 34 42 123 234 341 432 1234
#파이썬에 조합 관련 메소드가 있나?
from itertools import permutations , combinations
from itertools import product
print(combinations(example , 2))
#print(a)
##print(min(list) * len(list))


#4가지 경우 1 2 3 4 min * n개 or max값이고
# 2개면 가장 큰거 두개 min * 2개뽑는
# 3개도 가장 큰거 3개에서 min * 3
#4개는 min * 4개
#여기서 최대값을 구하면 되자나?
