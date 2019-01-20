'''
先行順巡回（Preorder Tree Walk):根節点、左部分木、右部分木
中間順巡回（Inorder Tree Walk) :左部分木、根節点、右部分木
後行順巡回（Postorder Tree Walk):左部分木、右部分木、根節点
'''

import sys
p = sys.stdout.write

NIL = -1
MAX = 100005

T = [None] * MAX

class Node:
    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL

n = int(input())

def preparse(u):
    if u == NIL:
        return
    p(str(u))
    preparse(T[u].left)
    preparse(T[u].right)

def inparse(u):
    if u == NIL:
        return
    inparse(T[u].left)
    p(str(u))
    inparse(T[u].right)

def postparse(u):
    if u == NIL:
        return
    postparse(T[u].left)
    postparse(T[u].right)
    p(str(u))

for i in range(n):
    T[i] = Node()

for i in range(n):
    _p, l, r = map(int, input().split())
    T[i].left = l
    T[i].right = r
    if l != NIL:
        T[l].parent = _p
    if r != NIL:
        T[r].parent = _p

root = -1
for i in range(n):
    if T[i].parent == NIL:
        root = i

print("Preorder")
preparse(0)
print()
print("Inordr")
inparse(0)
print()
print("Postorder")
postparse(0)
print()
