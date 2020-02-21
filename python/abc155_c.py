N = int(input())

counter = {}
max_count = 0
for _ in range(N):
    s = input()
    n = counter.get(s, 0) + 1
    max_count = max(max_count, n)
    counter[s] = n

most_common = (k for k, v in counter.items() if v == max_count)
for s in sorted(most_common):
    print(s)
