# from re import S


# n = int(input())


# str = list(input())
# sum = 0
# for i in range(n):
#     sum += int(str[i])

# print(sum)
#변환하는것이 ord 문자를 숫자로 &  나 chr 문자로

# a = list(input())

# if a[0].isdigit():
#     print(chr(a[0]))
# else:
#     print(ord(a[0]))

#결론 둘다 문자로 받아서 0~9 까지 그리고 각자 알파벳 기호로 바뀌니 ord가 대응하는 숫자로 변환
#chr은 기존 숫자를 해당 문자로 변환

#즉 두줄로 끝날꺼였다....
a = input()
print(ord(a))
