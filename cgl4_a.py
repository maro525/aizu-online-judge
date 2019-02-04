# -*- coding: utf-8 -*-
'''
凸包
アンドリューのアルゴリズム
'''

import collections
import math


class Vector2(collections.namedtuple("Vector2", ["x",  "y"])):

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __pos__(self):
        return Vector2(+self.x, +self.y)

    def __abs__(self):  # norm
        return math.sqrt(float(self.x * self.x + self.y * self.y))

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def abs2(self):
        return float(self.x * self.x + self.y * self.y)

    def dot(self, other):  # dot product
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # cross product
        return self.x * other.y - self.y * other.x


def getDistanceSP(segment, point):
    p = point
    p1, p2 = segment
    if (p2 - p1).dot(p - p1) < 0:
        return abs(p - p1)
    if (p1 - p2).dot(p - p2) < 0:
        return abs(p - p2)
    return abs((p2 - p1).cross(p - p1)) / abs(p2 - p1)


def getDistance(s1, s2):
    a, b = s1
    c, d = s2
    if intersect(s1, s2):  # intersect
        return 0
    return min(getDistanceSP(s1, c), getDistanceSP(s1, d), getDistanceSP(s2, a), getDistanceSP(s2, b))


def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if a.cross(b) > 0:
        return 1  # COUNTER_CLOCKWISE
    elif a.cross(b) < 0:
        return -1  # CLOCKWISE
    elif a.dot(b) < 0:
        return 2  # ONLINE_BACK
    elif abs(a) < abs(b):
        return -2  # ONLINE_FRONT
    else:
        return 0  # ON_SEGMENT


def intersect(s1, s2):
    a, b = s1
    c, d = s2
    return ccw(a, b, c) * ccw(a, b, d) <= 0 and ccw(c, d, a) * ccw(c, d, b) <= 0


def project(l, p):
    p1, p2 = l
    base = p2 - p1
    hypo = p - p1
    return p1 + base * (hypo.dot(base) / abs(base)**2)


class Circle():
    def __init__(self, c, r):
        self.c = c
        self.r = r


def getCrossPoints(c, l):
    pr = project(l, c.c)
    p1, p2 = l
    e = (p2 - p1) / abs(p2 - p1)
    base = math.sqrt(c.r * c.r - (pr - c.c).abs2())
    return [pr + e * base, pr - e * base]

def polar(r, a):
    return Vector2(r * math.cos(a), r * math.sin(a))

def getCrossPointsCircle(c1, c2):
    base = c2.c - c1.c
    d = abs(base)
    a = math.acos((c1.r**2 + d**2 - c2.r**2) / (2 * c1.r * d))
    t = math.atan2(base.y, base.x)
    return [c1.c + polar(c1.r, t + a), c1.c + polar(c1.r, t-a)]

def contains(g, p):
    n = len(g)
    x = 0
    for i in range(n):
        a = g[i] - p
        b = g[(i + 1) % n] - p
        if a.cross(b) == 0 and a.dot(b) <= 0:
            return 1
        if a.y > b.y:
            a, b = b, a
        if a.y <= 0 and b.y > 0 and a.cross(b) > 0:
            x += 1

    if x % 2 == 1:
        return 2
    else:
        return 0

def andrewScan(s):
    u = []
    l = []
    s = sorted(s, key=lambda x: (x.x, x.y))
    if len(s) < 3:
        return s
    u.append(s[0])
    u.append(s[1])
    l.append(s[-1])
    l.append(s[-2])

    for i in range(2, len(s)):
        for n in range(len(u), 1, -1):
            if ccw(u[n - 2], u[n - 1], s[i]) != 1:
                break
            else:
                u.pop()
        u.append(s[i])

    for i in range(len(s)-3, -1, -1):
        for n in range(len(l), 1, -1):
            if ccw(l[n-2], l[n-1], s[i]) != 1:
                break
            else:
                l.pop()
        l.append(s[i])

    ans = l + u[1:-1]
    ans.reverse()
    return ans

if __name__ == '__main__':

    n = int(input())
    s = []
    for _ in range(n):
        a, b = map(int, input().split())
        s.append(Vector2(a, b))
    ans = andrewScan(s)
    index = ans.index((min(ans, key=lambda x: x.y)))
    print(len(ans))
    for i in range(len(ans)):
        p = ans[(index + i) % len(ans)]
        print(p.x, p.y)
