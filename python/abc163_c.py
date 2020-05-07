import collections

N = int(input())
A = map(int, input().split())

counter = collections.Counter(A)
for i in range(1, N + 1):
    print(counter[i])
