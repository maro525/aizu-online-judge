n = int(input())
S = list(map(int, input().split()))

def partition(p, r):
    global n
    x = S[r]
    i = p - 1
    for j in range(p, r):
        if S[j] <= x:
            i += 1
            S[i], S[j] = S[j], S[i]
        else:
            j += 1
    S[r], S[i+1] = S[i+1], S[r]
    return i+1

q = partition(0, n-1)

for i in range(n):
    if i == q:
        print("[" + str(S[i]) + "]", end=" ")
    else:
        print(S[i], end=" ")
