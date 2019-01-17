# INF = int(float('inf'))
import sys
import math
INF = int(sys.maxsize)
cnt = 0

n = int(input())
S = list(map(int, input().split()))

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [A[left+i] for i in range(n1)] + [INF]
    R = [A[mid+i] for i in range(n2)] + [INF]
    global cnt
    i = j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
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

mergeSort(S, 0, n)
print(S)
print(cnt)
