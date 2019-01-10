from copy import copy
n = int(input())
a = [x for x in input().split(' ')]
b = copy(a)

def bubbleSort(A, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if A[j][1] < A[j-1][1]:
                A[j], A[j-1] = A[j-1], A[j]

def selectionSort(B, N):
    for i in range(N):
        min = i
        for j in range(i, N):
            if B[j][1] < B[min][1]:
                min = j
        B       [i], B[min] = B[min], B[i]

def isStable(A, B, N):
    for i in range(N):
        if A[i][0] != B[i][0]:
            return 'Not Stable'
    return "Stable"

bubbleSort(a, n)
selectionSort(b, n)

print(" ".join(a))
print("Stable")
print(" ".join(b))
print(isStable(a, b, n))
