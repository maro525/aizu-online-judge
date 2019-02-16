'''
ハッシュ
'''

M = 10464739
H = [''] * M

def getChar(ch):
    if ch == 'A':
        return 1
    elif ch == 'C':
        return 2
    elif ch == 'G':
        return 3
    elif ch == 'T':
        return 4
    else:
        return 0

def getKey(s):
    sum = 0
    p = 1
    for ch in s:
        sum += p * getChar(ch)
        p *= 5
    return sum

def h1(key):
    return key % M

def h2(key):
    return 1 + (key % (M - 1))

def hhh(key, i):
    return (h1(key) + i*h2(key)) % M

def find(s):
    key = getKey(s)
    i = 0
    while 1:
        h = hhh(key, i)
        if H[h] == s:
            return 1
        elif len(H[h]) ==0:
            return 0
        i += 1
    return 0

def insert(s):
    key = getKey(s)
    i = 0
    while 1:
        h = hhh(key, i)
        if H[h] == s:
            return 1
        elif len(H[h]) == 0:
            H[h] = s
            return 0
        i += 1
    return 0

n = int(input())

for x in range(n):
    com, s = input().split()
    if com[0] == 'i':
        insert(s)
    else:
        if find(s):
            print('yes')
        else:
            print('no')
