'''
シェルソート
'''

n = int(input())
a = [input() for _ in range(n)]

cnt = 0
G = []

def insertionSort(A, N, G):
    global cnt
    for i in range(G, N):
        v = A[i]
        j = i - G
        while j >= 0 and A[j] > v:
            A[j + G] = A[j]
            j = j - G
            cnt += 1
        A[j + G ] = v

def shellSort(A, N):
    h = 1
    while 1:
        if h > N:
            break
        G.append(h)
        h = 3 * h + 1

    for i in range(len(G)-1, -1, -1):
        insertionSort(A, N, G[i])

shellSort(a,n)

print(len(G))
print(" ".join(map(str, G)))
print(cnt)
print("\n".join(map(str, a)))
