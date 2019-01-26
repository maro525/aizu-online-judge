'''
dlp
動的計画法

最長共通部分列を求める
'''

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    X = " " + X
    Y = " " + Y

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        x = input()
        y = input()
        print(lcs(x, y))
