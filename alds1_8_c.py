'''
二分探索木
削除
'''
import sys
p = sys.stdout.write

class Node:
    def __init__(self, _d):
        self.data = _d
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
        else:
            while True:
                x = n.data
                if data < x:
                    if n.left is None:
                        n.left = Node(data)
                        n.left.parent = n
                        return
                    n = n.left
                else:
                    if n.right is None:
                        n.right = Node(data)
                        n.right.parent = n
                        return
                    n = n.right

    def find(self, k):
        u = self.root
        while u is not None and k != u.data:
            if u.data > k:
                u = u.left
            else:
                u = u.right
        return u

    def delete(self, k):
        if k.left is None or k.right is None:
            y = k
        else:
            y = self.getSuccessor(k)

        if y.left is not None:
            x = y.left
        else:
            x = y.right

        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != k:
            k.key = y.key

    def getSuccessor(self, k):
        if k.right is not None:
            return self.getMinimum(k.right)

        y = k.parent
        while y is not None and k == y.right:
            k = y
            y = y.parent
        return y


    def getMinimum(self, k):
        while k.left is not None:
            k = k.left
        return k

    def inorder(self, n):
        if n is not None:
            self.inorder(n.left)
            p(str(n.data) + ' ')
            self.inorder(n.right)

    def preorder(self,n):
        if n is not None:
            p(str(n.data) + ' ')
            self.preorder(n.left)
            self.preorder(n.right)

n = int(input())
bst = BST()

for i in range(n):
    k = input()
    if k[0] == "i":
        _, a = k.split()
        bst.insert(int(a))
    elif k[0] == "p":
        bst.inorder(bst.root)
        p('\n')
        bst.preorder(bst.root)
        p('\n')
    elif k[0] == "f":
        _, a = k.split()
        f = bst.find(int(a))
        if f is not None:
            print('yes')
        else:
            print('no')
    elif k[0] == "d":
        _, a = k.split()
        z = bst.find(int(a))
        bst.delete(z)
