n = int(input())
a = [input for _ in range(n)]

cnt = 0
G = []

def insertionSort(A, N, G):
    global cnt
    for i in range(G, N):
        v = A[i]
        j = i - G
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v

def shellSort(A, N):
    h = 1
    while 1:
        if h > n:
            break
        G.append(h)
        h = 3 * h + 1

    for i in range(len(G)-1, -1, -1):
        insertionSort(A, n, G[i])

shellSort(a,n)

print(len(G))
print(" ".join(map(str, G)))
print(cnt)
print("\n".join(map(str, A)))
