'''
反転数を計算する（Ai>Aj かつ i<Jであるものの数）
※反転数=バブルソートの交換回数
マージソートと似た分割統治法によって解く
'''

n = int(input())
a = list(map(int, input().split()))

import sys
INF = int(sys.maxsize)

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [A[left+i] for i in range(n1)] + [INF]
    R = [A[mid+i] for i in range(n2)] + [INF]
    i = j = cnt = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            cnt += n1-i
    return cnt

def mergeSort(A, left, right):
    if left+1 < right:
        mid = int((left+right) / 2)
        v1 = mergeSort(A, left, mid)
        v2 = mergeSort(A, mid, right)
        v3 = merge(A, left, mid, right)
        return v1 + v2 + v3
    else:
        return 0

print(mergeSort(a, 0, n))
print(a)
