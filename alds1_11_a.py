'''
グラフの表現
隣接リスト
'''

if __name__ == '__main__':

    n = int(input())
    M = [[0 for _ in range(n)] for a in range(n)]

    for i in range(n):
        l = list(map(int, input().split()))
        if l[1] == 0:
            continue
        for k in l[2:]:
            M[i][k-1] = 1

    for x in M:
        print(" ".join(map(str, x)))
