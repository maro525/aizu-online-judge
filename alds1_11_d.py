'''
連結成分
'''

if __name__ == '__main__':
    n, m = [int(s) for s in input().split(" ")]
    M = [set() for j in range(n)]
    for _ in range(m):
        u, v = [int(s) for s in input().split()]
        M[u].add(v)
        M[v].add(u)

    color = [0] * n

    def dfs(u, c):
        color[u] = c
        # print("color{} = {}".format(u, c))
        for v in M[u]:
            if color[v] == 0:
                dfs(v, c)

    # assign colors
    c = 1
    for u in range(n):
        if color[u] == 0:
            dfs(u, c)
            c += 1

    l = int(input())
    for _ in range(l):
        p, q = [int(s) for s in input().split()]
        if color[p] == color[q]:
            print("yes")
        else:
            print("no")
