N = int(input())
P = [int(x) for x in input().split()]

count = 0
min_p = N + 1
for p in P:
    min_p = min(min_p, p)
    if p <= min_p:
        count += 1

print(count)
