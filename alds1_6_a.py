n = int(input())
S = list(map(int, input().split()))

INF = 2000000

C = [0]*INF
A = [None] * n

for s in S:
    C[s] += 1

for i in range(1, len(C)):
    C[i] += C[i-1]

for a in range(n-1, -1, -1):
    A[C[S[a]]-1] = S[a]
    C[S[a]] -= 1

print(" ".join(map(str, A)))
