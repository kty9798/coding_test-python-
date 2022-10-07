import sys
input = sys.stdin.readline

N = int(input())
arr= list(map(int, input().split()))
#list로 캐스팅한건가

dp = [0] * N
for i in range(0 , N):
    #만약에  
    if i==0:
        dp[i] = arr[i]

    else:
        #초기화하고 그냥이 나은지 혹은 이전꺼랑 같이 하는게 나은지
        dp[i] = max(arr[i] , arr[i]+ dp[i-1])

print(max(dp))
#1 2 3 5 -8
# 0 -> 1 dp[0]
# 1  dp[1] 5
# dp[2] 10
# dp[3] = max(-8 ,  -8 + 10 = 2)
# dp[3] == 2 
# dp[2, ,5, 10 , 2] 중 max

# -1 -2 -3 -4 -5

