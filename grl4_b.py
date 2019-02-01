'''
トポロジカルソート
幅優先と深さ優先の両方の方法
DAG : 有向非巡回グラフ
'''
from collections import deque

if __name__ == '__main__':

    n, m = [int(s) for s in input().split()]
    E = [set() for _ in range(n)]
    for _ in range(m):
        s, t = [int(s) for s in input().split()]
        E[s].add(t)

    def bfs(s):
        Q.append(s)
        color[s] = 1
        out.append(u)
        while Q:
            u = Q.popleft()
            out.append(u)
            for v in E[u]:
                indev[v] -= 1
                if indev[v] == 0 and color[v] == 0:
                    color[v] = 1
                    Q.append(v)

    def topological_sort():
        global n, E
        color = [0] * n
        indeg = [0] * n
        for s in range(n):
            for t in E[s]:
                indeg[t] += 1

        Q = deque()
        out = []

        for u in range(n):
            if indeg[u] == 0 and color[u] == 0:
                bfs(u)

        print("\n".join(map(str, out)))

    topological_sort()
