n = int(input())
stack = []
answer = []
flag = 0
cur = 1

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur +=1
    #입력 수를 만나고 그거 보다 크면 빼야되니

    #마지막이랑 num값이 같으면 안같은데 뺄순 없으니가
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break


if flag ==0:
    for i in answer:
        print(i)