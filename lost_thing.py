get_string = input().split(sep = "-")

#     -     
#ex[55 40+50]
result = 0
#다 +만 있고 -로 나눴으니까
for i in get_string[0].split("+"):
    result += int(i)

#50+40-50-50-50-50
#90 
#50+40 (-) 50 +50 (-) 50 (-) 50 (-) 50
#-가 나오면 최대한 -가 나올때까지 더해서 뺸다
#끝
#a , b, c, d
#50+40 이니까 
for i in get_string[1:]:
    for j in i.split("+"): #50 , 40들을 빼
        result -= int(j)

print(result)
