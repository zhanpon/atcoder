N = int(input())
A = [int(x) for x in input().split()]

mapping = {ai : i for i, ai in enumerate(A, 1)}
print(" ".join(str(mapping[ai]) for ai in range(1, N + 1)))
