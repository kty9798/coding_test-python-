#문자를 받는다
#다 소문자로 만든다음에
#아스키 코드 변환으로 리스트에 값을 넣어주고
#가장 높은 숫자의 값을 출력하면 끝



b = str(input())
#c =b.lower()
c = b.split(" ")
len_c = len(c)
delete_index = []
for i in range(len_c):
    if c[i] =="":
        delete_index.append(i)

print(len(c) - len(delete_index))

#c는 문자열

#총 26개의 알파벳
#아스키코드로 바꿔서
'''result = 26 *[0]
for i in range(len(c)):
    index = (ord(c[i]) - 97) #a면 0 65 90까지 
    result[index] += 1'''
#단어새는거
#print(max(result))
#소수점은 97부터
#print(max(result))
