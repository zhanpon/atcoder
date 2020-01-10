def lcm(m: int, n: int) -> int:
    for x in range(m, n * m + 1, m):
        if x % n == 0:
            return x


A, B = [int(x) for x in input().split()]
print(lcm(A, B))
