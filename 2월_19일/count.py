a =[-2 , 1 , 2, 3, 8]
#빈도수 구하기 위해서

from collections import Counter



def get_freq(sorted_list):
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
    result = Counter(a)
    #print(result)

