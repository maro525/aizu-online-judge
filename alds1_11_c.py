'''
幅優先探索
'''
from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2


if __name__ == '__main__':
    n = int(input())
    M = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        l = list(map(int, input().split()))
        if l[1] == 0:
            continue
        for k in l[2:]:
            M[i][k-1] = 1

    color = [0] * n
    d = [0] * n
    Q = deque()

    def bfs(s):
        color[s] = GRAY
        d[s] = 0
        Q.append(s)

        while len(Q) != 0:
            u = Q.popleft()
            for v in range(n):
                if M[u][v] == 1 and color[v] == WHITE:
                    color[v] = GRAY
                    d[v] = d[u] + 1
                    Q.append(v)
            color[u] = BLACK

    bfs(0)
    for i in range(n):
        print(i+1, d[i])
