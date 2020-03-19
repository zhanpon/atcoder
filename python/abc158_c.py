import math


def solve(a, b):
    for i in range(2000):
        if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
            return i

    return -1


A, B = map(int, input().split())

print(solve(A, B))
