import collections


def distances(n, x, y):
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            yield min(j - i, abs(x - i) + abs(y - j) + 1)


N, X, Y = map(int, input().split())

c = collections.Counter(distances(N, X, Y))

for i in range(1, N):
    print(c[i])
