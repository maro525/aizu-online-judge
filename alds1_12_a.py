'''
最小全域木
Minimym Spanning Tree
'''

BLACK = 2
GRAY = 1
WHITE = 0

if __name__ == '__main__':

    n = int(input())
    M = [list(map(int, input().split())) for i in range(n)]

    color = [0] * n
    weight = [float("inf")] * n
    parent = [None] * n

    def prim():
        weight[0] = 0
        parent[0] = -1

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
                if color[v] != BLACK and M[u][v] != -1:
                    if M[u][v] < weight[v]:
                        weight[v] = M[u][v]
                        parent[v] = u
                        color[v] = GRAY

    prim()

    sum = 0
    for i in range(n):
        if parent[i] != -1:
            sum += M[i][parent[i]]

    print(sum)
