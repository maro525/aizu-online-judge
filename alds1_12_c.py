'''
単一始点最短経路

ダイクストラのアルゴリズム
ヒープを用いて計算量削減
'''

from heapq import heappush, heappop

BLACK = 2
GRAY = 1
WHITE = 0

if __name__ == '__main__':

    n = int(input())
    M = [set() for i in range(n)]

    for i in range(n):
        l = list(map(int, input().split(" ")))
        for k in range(l[1]):
            j = l[2 + 2*k]
            c = l[2 + 2*k + 1]
            M[i].add((j, c))

    weight = [float("inf")] * n
    h = []

    def dijkstra(s):
        color = [0] * n
        parent = [None] * n

        weight[s] = 0
        heappush(h, (weight[s], s))

        while h:
            _, u = heappop(h)

            color[u] = 2

            for v, c in M[u]:
                if color[v] != BLACK:
                    if weight[u] + c < weight[v]:
                        weight[v] = weight[u] + c
                        color[v] = 1
                        heappush(h, (weight[v], v))

    dijkstra(0)

    for i in range(n):
        print(i, weight[i])
