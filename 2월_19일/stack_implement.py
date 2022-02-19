import sys
input = sys.stdin.readline


class stack:
    def __init__(self):
        self.list = []

    def push(self , element):
        self.list.append(element) #self를 넣어줘야돼?

    def size(self):
        print(len(self.list))

    def top(self):
        if len(self.list) != 0:
            print(self.list[-1])
        else:
            print(-1)

    def empty(self):
        if len(self.list) ==0:
            print(1)
        else:
            print(0)
        
    def _pop(self):
        if len(self.list) !=0:
            print(self.list.pop())
        else:
            print(-1)

stack = stack()

n = int(input())

for i in range(n):
    a  = list(input().split())
    if a[0] == "push":
        stack.push(a[1])
    elif a[0] == "top":
        stack.top()
    elif a[0] == "size":
        stack.size()
    elif a[0]== "empty":
        stack.empty()
    else:
        stack._pop()

