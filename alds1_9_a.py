'''
完全二分木で表された二分ヒープ
max ヒープ条件 : 節点のキーがその親のキー以下である
min ヒープ条件 : 節点のキーがその親のキー以上である
'''

import sys
p = sys.stdout.write

def parent(i):
    return int(i/2)

def left(i):
    return i * 2;

def right(i):
    return i * 2 + 1

n = int(input())
A = [None] + [int(i) for i in input().split(" ")]

for i in range(1, n+1):
    p("node {}: key = {},".format(i, A[i]))
    if parent(i) >= 1:
        p("parent key = {},".format(A[parent(i)]))
    if left(i) <= n:
        p("left key = {},".format(A[left(i)]))
    if right(i) <= n:
        p("right key = {},".format(A[right(i)]))
    p("\n")
