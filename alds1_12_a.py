'''
最小全域木
Minimym Spanning Tree
'''

if __name__ == '__main__':

    n = int(input())
    M = [list(map(int, input().split())) for i in range(n)]

    used = [False] * n
    mincost = [float("inf")] * n

    def prim():
        mincost[0] = 0
        sum = 0

        while True:
            v = -1
            for i in range(n):
                if (not used[i]) and (v == -1 or mincost[i] < mincost[v]):
                    v = i
            if v == -1:
                break
            used[v] = True
            sum += mincost[v]
            print(sum)
            for i in range(n):
                mincost[i] = min(mincost[i], M[v][i])

        return sum

    print(prim())
