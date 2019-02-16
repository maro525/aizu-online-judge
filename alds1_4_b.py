'''
二分探索
'''

import sys
input = sys.stdin.readline

sn = int(input())
sa = list(map(int, input().split()))
tn = int(input())
ta = list(map(int, input().split()))

cnt = 0

for t in ta:
    left = 0
    right = sn
    while left < right:
        mid = int((left+right)/2)
        print(mid)
        if sa[mid] == t:
            cnt += 1
            break
        elif sa[mid] > t:
            right = mid
        else:
            left = mid+1

print(cnt)
