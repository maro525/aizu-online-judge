class Stack:
    def __init__(self, max_size=100):
        self.top = 0
        self.array = [None]*(max_size+1)
        self.bufferMax = (max_size+1)

    def initialize(self):
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def isFull(self):
        return self.top >= self.bufferMax-1

    def push(self, data):
        if self.isFull():
            print("stack is full")
            return

        self.top += 1
        self.array[self.top] = data

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return

        self.top -= 1
        return self.array[self.top+1]

array = [x for x in input().split(' ')]
s = Stack(max_size = len(array))

for a in array:
    # if a.isdigit():
    if type(int(a)) == 'int':
        s.push(int(a))
    elif a == "+":
        x = s.pop()
        y = s.pop()
        s.push(x+y)
    elif a == "-":
        x = s.pop()
        y = s.pop()
        s.push(y-x)
    elif a == "*":
        x = s.pop()
        y = s.pop()
        s.push(x*y)
    elif a == "/":
        x = s.pop()
        y = s.pop()
        s.push(y/x)

print(s.pop())
