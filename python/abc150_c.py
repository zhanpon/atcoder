from itertools import permutations

N = int(input())
P = tuple(int(x) for x in input().split())
Q = tuple(int(x) for x in input().split())

ps = permutations(range(1, N + 1))

try:
    x, y = [i for i, t in enumerate(ps) if t == P or t == Q]
except ValueError:
    print(0)
else:
    print(abs(x - y))
