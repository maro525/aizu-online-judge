'''
Maxヒープの作成
'''

def parent(i):
    return i // 2

def left(i):
    return i * 2;

def right(i):
    return i * 2 + 1

def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest  i
    if r <= n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)

n = int(input())
A = [None] + [int(i) for i in input().split(" ")]

for i in range(n//2, 0, -1):
    maxHeapify(A, i)
