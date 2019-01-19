'''
クイックソート
分割統治法に基づくアルゴリズム。ただし、統治がない
安定ではない、インプレースソート
兵員の計算量O(nlogn)
https://github.com/maro525/aizu-online-judge/blob/master/alds1_46_b.pyのパーティションを使う 
'''

import sys
INF = sys.maxsize

class Card:
    def __init__(self, s, v):
        self.suit = s
        self.value = v

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [A[left+i] for i in range(n1)]
    L.append(Card('dummy', INF))
    R = [A[mid+i] for i in range(n2)]
    R.append(Card('dummy', INF))
    i = j = 0
    for k in range(left, right):
        if L[i].value <= R[j].value:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

def partition(A, p, r):
    x = A[r].value
    i = p - 1
    for j in range(p, r):
        if A[j].value <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
        else:
            j += 1
    A[r], A[i+1] = A[i+1], A[r]
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

n = int(input())
X = [None] * n
Y = [None] * n

for i in range(n):
    s, v = input().split()
    X[i] = Card(s, int(v))
    Y[i] = Card(s, int(v))

mergeSort(X, 0, n-1)
quicksort(Y, 0, n-1)

if X == Y:
    print('Stable')
else:
    print('Not Stable')

for y in Y:
    print(y.suit, " ", y.value)
