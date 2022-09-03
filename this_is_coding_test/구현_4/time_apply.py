from time import time
n = int(input())


result = 0

start_time= time()

#ex 0 이면 23이면 
for number in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(number) + str(m) + str(s):
                result+=1

end_time = time()
print(result)