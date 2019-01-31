'''
単一始点最短経路

ダイクストラのアルゴリズム
'''

BLACK = 2
GRAY = 1
WHITE = 0

if __name__ == '__main__':

    n = int(input())
    M = [[float("inf") for j in range(n)] for i in range(n)]

    for i in range(n):
        l = list(map(int, input().split(" ")))
        for k in range(l[1]):
            j = l[2 + 2*k]
            c = l[2 + 2*k + 1]
            M[i][j] = c

    color = [0] * n
    weight = [float('inf')] * n
    parent = [None] * n

    weight = [float('inf')] * n

    def dijkstra(s):
        color = [0] * n
        parent = [None] * n

        weight[s] = 0
        parent[s] = -1

        while True:
            mincost = float("inf")
            for i in range(n):
                if color[i] != BLACK and weight[i] < mincost:
                    mincost = weight[i]
                    u = i

            if mincost == float("inf"):
                break

            color[u] = BLACK

            for v in range(n):
                if color[v] != BLACK:
                    if weight[u] + M[u][v] < weight[v]:
                        weight[v] = weight[u] + M[u][v]
                        parent[v] = u
                        color[v] = GRAY


    dijkstra(0)

    for i in range(n):
        print(i, weight[i])
