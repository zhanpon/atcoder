from itertools import combinations
from math import sqrt, floor, ceil


def is_square_of_int(n):
    f = sqrt(n)
    return floor(f) ** 2 == n or ceil(f) ** 2 == n


def square_distance(p1, p2):
    return sum((x1 - x2) ** 2 for x1, x2 in zip(p1, p2))


N, D = map(int, input().split())
X = []

for _ in range(N):
    X.append([int(x) for x in input().split()])

answer = sum(
    1 for p1, p2 in combinations(X, 2) if is_square_of_int(square_distance(p1, p2))
)
print(answer)
