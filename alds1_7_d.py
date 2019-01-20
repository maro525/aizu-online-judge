'''
二分木の復元
与えられたPreorderとinorderから、postorderを算出する
'''
n = int(input())
prearray = list(map(int, input().split()))
inarray = list(map(int, input().split()))
post = []

pos = 0

def rec(l, r):
    if l >= r:
        return
    global pos
    root = prearray[pos]
    pos += 1
    ind = inarray.index(root)
    rec(l, ind)
    rec(ind+1, r)
    post.append(root)

rec(0, len(prearray))
print(" ".join(map(str, post)))
