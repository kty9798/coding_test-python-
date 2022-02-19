from collections import Counter

def get_freq(sorted_list):
    freq_value = 0
    result = Counter(sorted_list)
    
    freq_result = list(result.values()) #key와 values
#유일하다면
        
    max_value = max(freq_result)#같은 값이 있을때 처음 값
    
    same_value = 0
    for i in range(len(result)): #key값을 뽑아내는거지
        if result[list(result.keys())[i]] == max_value:
            same_value+=1
            same_index = list(result.keys())[i]
            if same_value ==2:
                freq_value = list(result.keys())[i]
                break
            
    if same_value ==1:
        freq_value = same_index #key
        
    return freq_value

n = int(input())
#lstrip rstrip 개행 없애는것
a = []
b = 0

for i in range(n):
    b = int(input())
    a.append(b)

a = sorted(a)
#print(sum(list)//5)
mean = int(round(sum(a)/n))
#index가 0 1 2 3 4 즉 len-1/2
# 0 1-1/2
index = int((len(a)-1)/2)
median = a[index]
freq = get_freq(a)
length = a[-1] - a[0]

print(mean)
print(median)
print(freq)
print(length)

#print(list)







