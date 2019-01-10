class Queue:
    def __init__(self, max_size=10):
        self.bufferMax = max_size+1
        self.head = 0
        self.tail = 0
        self.index = -1
        self.array = [None]*(max_size+1)

    def initialize(self):
        self.head = self.tail = 0

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return self.head == ((self.tail+1) % self.bufferMax)

    def enqueue(self, data):
        if self.isFull():
            print("queue is full")
            return

        self.array[self.tail] = data
        self.tail = (self.tail+1) % self.bufferMax

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return

        data = self.array[self.head]
        self.head = (self.head+1) % self.bufferMax
        return data

class P:
    def __init__(self, n, t):
        self.name = n
        self.time = t

def min(a, b):
    return a if a < b else b

n, a = map(int, input().split(" "))

q = Queue(max_size=n)

elapse = 0

for i in range(n):
    name, time = input().split(" ")
    p = P(name, int(time))
    q.enqueue(p)

while not q.isEmpty():
    x = q.dequeue()
    t = min(x.time, a)
    x.time -= t
    elapse += t
    if x.time > 0:
        q.enqueue(x)
    else:
        print(x.name, elapse)
