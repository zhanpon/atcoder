def is_valid(n, conditions):
    ns = [int(i) for i in str(n)]
    return all(ns[s - 1] == c for s, c in conditions)


N, M = map(int, input().split())

sc = []
for _ in range(M):
    s, c = map(int, input().split())
    sc.append((s, c))

candidates = (i for i in range(1000) if len(str(i)) == N and is_valid(i, sc))

try:
    print(next(candidates))
except StopIteration:
    print(-1)
