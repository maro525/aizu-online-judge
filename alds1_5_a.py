import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

S = [None] * n
for i in range(n):
    S[i] = 0

def rec(i):
    if i == n:
        print(S)
        return

    rec(i+1)
    S[i] = 1
    rec(i+1)
    S[i] = 0

rec(0)
