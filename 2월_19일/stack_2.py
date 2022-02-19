import sys
input =sys.stdin.readline


class stack:
    def __init__(self):
        self.item = []
        self.no_error = True

    def empty(self):
        return True if len(self.item) ==0 else False

    def push(self , element):
        self.item.append(element)

    def _pop(self):
        if len(self.item)==0:
            self.no_error = False
            
        else:
            self.item.pop()
    
    def delete(self):
        self.item.clear()
        self.no_error = True

result = []        
n = int(input())
stack = stack()
for i in range(n):
    a = list(input().rstrip()) #개행을 없애줘야하는구나
    
    #print(a)
    for i in range(len(a)):
        if a[i] == "(":
            stack.push(a[i])
        else:
            stack._pop()

    #print(stack.no_error)
    if stack.empty() and stack.no_error:
        result.append("YES")
    else:
        result.append("NO")
    stack.delete()

    
    

for i in result:
    print(i)
    