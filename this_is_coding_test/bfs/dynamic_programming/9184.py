
MAX= 21
dp = [[[0] *MAX  for _ in range(MAX)] for _ in range(MAX)]






def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] != 0:
        return dp[a][b][c]


    
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c]  = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]

if __name__ == "__main__":
    
    result = []
    while True:
        a, b, c = map(int , input().split())

        if a ==-1 and b== -1 and c==-1:
            break

        result.append((a,b,c, w(a,b,c)))
            
    for i in range(len(result)):
        print("w({}, {}, {}) = {}".format(str(result[i][0]) , str(result[i][1]) , str(result[i][2]) , str(result[i][3])))
