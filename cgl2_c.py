'''
線分の交点
Intersection
'''

import collections
import math

class Vector2(collections.namedtuple("Vector2", ["x", "y"])):

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

    def __abs__(self):
        return math.sqrt(float(self.x * self.x + self.y * self.y))

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
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
    if intersect(s1, s2):
        return 0
    return min(getDistanceSP(s1, c), getDistanceSP(s1, d), getDistanceSP(s2, a), getDistanceSP(s2, b))

def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if a.cross(b) > 0:
        return 1
    elif a.cross(b) < 0:
        return -1
    elif a.dot(b) < 0:
        return 2
    elif abs(a) < abs(b):
        return -2
    else:
        return 0

def intersect(s1, s2):
    a, b = s1
    c, d = s2
    return ccw(a, b, c) * ccw(a, b, d) <= 0 and ccw(c, d, a) * ccw(c, d, b) <= 0

def getCrossPoint(s1, s2):
    a, b = s1
    c, d = s2
    base = d - c
    d1 = abs(base.cross(a-c))
    d2 = abs(base.cross(b-c))
    t = d1 / (d1 + d2)
    return a + (b - a) * t

if __name__ == '__main__':

    n = int(input())

    for _ in range(n):
        l = list(map(int, input().split()))
        s1 = [Vector2(l[0], l[1]), Vector2(l[2], l[3])]
        s2 = [Vector2(l[4], l[5]), Vector2(l[6], l[7])]

        x = getCrossPoint(s1, s2)
        print(x.x, x.y)
