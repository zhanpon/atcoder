N, K, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

required_score = N * M - sum(A)
if required_score > K:
    print(-1)
else:
    print(max(0, required_score))
