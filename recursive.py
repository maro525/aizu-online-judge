n = int(input())
S = [None] * n
for i in range(n):
    S[i] = 0


def rec(i):
    if i == n:
        print(S)
        return
    # print(i)
    rec(i+1)
    S[i] = 1
    rec(i+1)
    S[i] = 0

rec(0)
