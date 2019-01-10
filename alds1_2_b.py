n = int(input())
a = [int(x) for x in input().split(' ')]

def selectionSort(A, N):
    cnt = 0
    for i in range(N):
        min = i
        for j in range(i, N):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
        if i != min:
            cnt += 1
    return cnt

cnt = selectionSort(a, n)
print(" ".join(map(str, a)))
print(n)
