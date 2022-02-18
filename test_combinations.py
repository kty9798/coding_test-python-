
# from itertools import combinations , permutations 
# a = ['1','2','3','4']

# result = list(combinations(a,2))
# print("**경우의 수 : %s개" % len(result))
# print(result)


from itertools import permutations , combinations
from itertools import product

example = ['1','2','3','4']
total = []
for i in range(1,len(example)+1):
    total.append(list(combinations(example , i)))
    


print(total[0][3])



#1개면 그냥 [2,4,2,2,3]