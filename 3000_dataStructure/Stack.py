### 파이썬에서 stack은 리스트로 구현한다.

stk = []
stk.append(1)
stk.append(2)

print(stk) # [1,2]
print(stk.pop()) # 2
print(stk.pop()) # 1

### 클래스로 stack 구현하기

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except:
            print("Stack is Empty")

stk = Stack()
print(stk)
stk.push(1)
stk.push(2)
print(stk.pop())
print(stk.pop())
print(stk.pop())