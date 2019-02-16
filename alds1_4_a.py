'''
線形探索
番兵を置いた線形探索
'''

import sys
input = sys.stdin.readline

sn = int(input())
sa = list(map(int, input().split()))
tn = int(input())
ta = list(map(int, input().split()))

cnt = 0

# for t in T:
#     if t in S:
#         c += 1

for t in ta:
    sa.append(t)
    i = 0
    while sa[i] != t:
        i+=1
    if i < len(sa)-1:
        cnt += 1
    sa.pop()

print(cnt)
