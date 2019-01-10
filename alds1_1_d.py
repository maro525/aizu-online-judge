n = int(input())
r0 = int(input())
maxv = -10000
minv = r0

for j in range(1,n):
    r = int(input())
    maxv = max(maxv, r - minv)
    minv = min(minv, r)

print('max = ',maxv)
