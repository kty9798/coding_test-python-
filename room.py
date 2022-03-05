import sys

#n = int(input())

time= [[0]*2 for _ in range(5)]

print(time)

x = [2,4]
b = (lambda x : x*2)(x)
print(b)

lamdas =[lambda x: x+10 , lambda x: x+100]
test =[2 * x for x in range(5)]
print(test)
#람다는 함수와 같다 lambda(5) 함수 쓰듯이