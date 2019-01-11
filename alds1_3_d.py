import sys
input = sys.stdin.readline

a = input()
n = len(a)
print(a)
area = 0
stk = [] # stack
p = [] # 面積

i = 0
for k in a:
    if k == '\\':
        stk.append(i)
    elif k == '/' and len(stk) > 0:
        x = stk.pop()
        a = i - x
        area += a
        while len(p) > 0 and p[-1][0] > x:
            a += p.pop()[1]
        p.append([x, a])
    i += 1

print(area)
print(len(p), end = "")
for i in p:
    print(' ' + str(i[1]), end="")

# \\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\
