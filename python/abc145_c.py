import math
from itertools import permutations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, p):
        dx = p.x - self.x
        dy = p.y - self.y
        return math.sqrt(dx * dx + dy * dy)


def route_distance(ps):
    if len(ps) < 2:
        return 0
    else:
        return ps[0].distance_to(ps[1]) + route_distance(ps[1:])


def main():
    N = int(input())
    ps = []
    for _ in range(N):
        x, y = map(int, input().split())
        ps.append(Point(x, y))

    sum_routes = sum(route_distance(ps) for ps in permutations(ps, N))
    print(sum_routes / math.factorial(N))


if __name__ == "__main__":
    main()
