n = int(input())

get =[]
output=[]
result=""
for i in range(n):
    a = str(input())
    num , things =a.split(" ")
    for i in range(len(things)):
        result += int(num) * things[i]
    
    output.append(result)
    result =""



for i in output:
    print(i)




