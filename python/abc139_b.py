A, B = map(int, input().split())

n = sum(1 for _ in range(1, B, A - 1))
print(n)
