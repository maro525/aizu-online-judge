'''
最小コストソート
重さがWiのn個のに持つが並んでいて、ロボットアームで並べ替える
荷物iと荷物jを取り替える場合、コストはWi+Wj
最小コストは？

隣で交換するものは隣で交換
長さが2以上に渡る交換では、最小の要素を使って交換する
反例として、サイクルの外から借りた要素を用いる方がコストが下がる場合が挙げられる
その場合のコストとも比較しておく
'''

from copy import copy

n = int(input())
a = list(map(int, input().split()))
s = min(a)

VMAX = 10000

def solve():
    ans = 0
    B = a.copy()
    V = [False for _ in range(n)]
    B.sort()
    T = [0] * (VMAX+1) # 正しいインデックスを入れる
    print(B)
    for i in range(n):
        T[B[i]] = i
    print(T)
    for i in range(n):
        if V[i]:
            continue
        cur = i
        S = 0 # sum of weight
        m = VMAX # min of circle
        an = 0 # length of cicle
        while 1:
            V[cur] = True
            print(V)
            an += 1
            v = a[cur]
            m = min(m, v)
            print("v = {}".format(v))
            S += v
            cur = T[v]
            print("cur = {}".format(cur))
            if V[cur]:
                break
        ans += min(S + (an-2) * m, m + S + (an+1) * s)
    return ans

print(solve())
