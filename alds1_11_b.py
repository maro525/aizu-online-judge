'''
深さ優先探索
'''

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
    f = [0] * n
    time = 0

    # 再帰による負荷左右選択作
    def dfs(u):
        global time
        color[u] = GRAY
        time += 1
        d[u] = time
        for v in range(n):
            if M[u][v] == 1 and color[v] == 0:
                dfs(v)
        color[u] = BLACK
        time += 1
        f[u] = time

    for u in range(n):
        if color[u] == WHITE:
            dfs(u)

    for x in range(n):
        print(x+1, d[x], f[x])
