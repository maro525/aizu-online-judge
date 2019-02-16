'''
探索の応用
最適解の計算
Allocation
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

MAX = 100000
left = 0
right = MAX * 10000

def check(P):
    i = 0
    for _ in range(k):
        s = 0
        while (s + w[i]) <= P:
            s += w[i]
            i += 1
            if i == n:
                return n
    return i

while right-1 > left:
    mid = int((left + right) / 2)
    v = check(mid)
    print(left,right,mid,v)
    if v >= n:
        right = mid
    else:
        left = mid

print(right)
