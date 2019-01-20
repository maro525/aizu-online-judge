'''
二分木の表現
'''

import sys
p = sys.stdout.write

NIL = -1
MAX = 100005

T = [None] * MAX
D = [0] * MAX
H = [0] * MAX

class Node:
    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL

def setDepth(u, d):
    if u == NIL:
        return
    D[u] = d
    setDepth(T[u].left, d+1)
    setDepth(T[u].right, d+1)

def setHeight(u):
    h1 = 0
    h2 = 0
    if T[u].left != NIL:
        h1 = setHeight(T[u].left) + 1
    if T[u].right != NIL:
        h2 = setHeight(T[u].right) + 1
    H[u] = h1 if h1 > h2 else h2
    return H[u]

def getSibling(u):
    if T[u].parent == NIL:
        return NIL
    _p = T[u].parent
    if T[_p].left != u and T[_p].left != NIL:
        return T[_p].left
    elif T[_p].right != u and T[_p].right != NIL:
        return T[_p].right
    return NIL

def printtree(u):
    p('node ' + str(u) + ': parent = ' + str(T[u].parent) + ', ')
    p('sibling = ' + str(getSibling(u)) + ', ')
    deg = 0
    if T[u].left != NIL:
        deg += 1
    if T[u].right != NIL:
        deg += 1
    p('degree = ' + str(deg) + ', ')
    p('depth = ' + str(D[u]) + ', ')
    p('height = ' + str(H[u]) + ', ')

    if T[u].parent == NIL:
        p('root\n')
    elif T[u].left == NIL and T[u].right == NIL:
        p('leaf\n')
    else:
        p('internal node\n')

n = int(input())
for i in range(n):
    T[i] = Node()

for i in range(n):
    _p,l,r = map(int, input().split())
    T[i].left = l
    T[i].right = r
    if l != NIL:
        T[l].parent = _p
    if r != NIL:
        T[r].parent = _p

root = 0
for i in range(n):
    if T[i].parent == NIL:
        root = i

setDepth(root, 0)
setHeight(root)

for i in range(n):
    printtree(i)
