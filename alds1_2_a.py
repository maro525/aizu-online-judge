def bubbleSort(A, N):
    flg = 1
    i = 0
    cnt = 0
    while flg:
        flg = 0
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flg = 1
                cnt += 1
        i += 1
    return cnt

n = int(input())
a = [int(x) for x in input().split(' ')]

c = bubbleSort(a, n)

print(" ".join(map(str, a)))
print(c)
