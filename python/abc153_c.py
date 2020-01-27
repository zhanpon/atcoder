from heapq import nsmallest

N, K = map(int, input().split())
H = (int(x) for x in input().split())

print(sum(nsmallest(N - K, H)))
