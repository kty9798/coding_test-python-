n = int(input())

a = list(input())
    
a_len = len(a)
    
for i in range(n-1):
    str = list(input())
    for j in range(a_len):
        if a[j] != str[j]:
            a[j] = "?"

print(str(a))