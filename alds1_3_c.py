'''
連結リスト
'''

import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    x = input()
    if x[0] == 'i':
        x,d = x.split()
        a.append(d)
    elif x[-4] == 'e':
        x, d = x.split()
        for j in range(len(a)-1, 0, -1):
            if a[j] == d:
                a.pop(j)
                break
    elif x[6] == 'F':
        a.pop()
    elif x[6] == 'L':
        a.pop(0)
    print(a)

print(" ".join(reversed(a)))
