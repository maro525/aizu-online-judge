n = int(input())
a = [int(x) for x in input().split(' ')]

def trace(A):
    print(" ".join(map(str, A)))

def insertionSort(A, N):
    for i in range(N):
        v = A[i]
        j = i-1
        while j >= 0 and A[j] >= v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        trace(A)

trace(a)
insertionSort(a, n)
