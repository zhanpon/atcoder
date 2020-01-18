N, K = map(int, input().split())
h = map(int, input().split())

print(sum(1 for x in h if x >= K))
