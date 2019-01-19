'''
根付き木の表現
'''
import sys
p = sys.stdout.write

NIL = -1
MAX = 100005

class Node:
    def __init__(self):
        self.p = NIL
        self.l = NIL
        self.r = NIL

T = [None] * MAX
D = [0] * MAX

def printtree(u):
    p('node ' + str(u) + ': paret = ' +
        str(T[u].p) + ', depth = ' + str(D[u]) + ', ')
    if T[u].p == NIL:
        p('root, ')
    elif T[u].l == NIL:
        p('leaf, ')
    else:
        p('internal node, ')
    p('[')
    c = T[u].l
    i = 0
    while c != NIL:
        if i:
            p(', ')
        p(str(c))
        c = T[c].r
        i += 1
    p(']\n')

def getDepth(u):
    d = 0
    while T[u].p != NIL:
        u = T[u].p
        d += 1
    return d

def setDepth(u,p):
    D[u] = p
    if T[u].r != NIL:
        setDepth(T[u].r, p)
    elif T[u].l != NIL:
        setDepth(T[u].l, p+1)

n = int(input())
for i in range(n):
    T[i] = Node()

for i in range(n):
    t = input().split()
    id, k = int(t[0]), int(t[1])
    l = 0
    for j in range(2, k+2):
        c = int(t[j])
        if j == 2:
            T[id].l = c
        else:
            T[l].r = c
        l = c
        T[c].p = id

for i in range(n):
    D[i] = getDepth(i)

for i in range(n):
    printtree(i)
