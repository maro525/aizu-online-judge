'''
二分探索木
探索
'''
import sys
p = sys.stdout.write

class Node:
    def __init__(self, _d):
        self.data = _d
        self.left = None
        self.right = None

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
                        return
                    n = n.left
                elif data > x:
                    if n.right is None:
                        n.right = Node(data)
                    n = n.right
                else:
                    n.data = data
                    return

    def find(self, k):
        u = self.root
        while u is not None and k != u.data:
            if u.data > k:
                u = u.left
            else:
                u = u.right
        return u

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
