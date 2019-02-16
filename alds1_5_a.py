'''
全探索
Exhaustive Search
'''

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

def solve(i, m):
    global n
    if m == 0:
        return 1
    if i >= n:
        return 0
    res = solve(i+1, m) or solve(i+1, m-A[i])
    return res

S = [None] * n

for i in range(q):
    if solve(0, T[i]):
        print("yes")
    else:
        print("no")
