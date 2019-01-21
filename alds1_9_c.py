'''
ヒープ
優先度付きキュー
'''

def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

class MaxHeap(list):
    def __init__(self, n=0):
        list.__init__(self)
        self.N = n
        self[:] = [None]

    def insert(self, key):
        self.N += 1
        self.append(-float("inf"))
        self.heapInceaseKey(self.N, key)

    def heapInceaseKey(self, i, key):
        if key < self[i]:
            return
        self[i] = key
        while i > 1 and self[parent(i)] < self[i]:
            _i = parent(i)
            self[i], self[_i] = self[_i], self[i]
            i = _i

    def heapExtract(self):
        if self.N < 1:
            raise "underflow"
        maximum = self[1]
        self[1] = self.pop()
        self.N -= 1
        self.maxHeapify(1)

        return maximum

    def maxHeapify(self, i):
        l = left(i)
        r = right(i)
        if l <= self.N and self[l] > self[i]:
            largest = l
        else:
            largest = i
        if r <= self.N and self[r] > self[largest]:
            largest = r

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.maxHeapify(largest)

if __name__ == '__main__':

    A = MaxHeap()
    while True:
        c = input().split()
        if c[0] == "insert":
            A.insert(int(c[1]))
        elif c[0] == "extract":
            print(A.heapExtract())
        else:
            break
