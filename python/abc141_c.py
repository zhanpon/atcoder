N, K, Q = map(int, input().split())
correct_count = [0 for _ in range(N)]

for _ in range(Q):
    ai = int(input())
    correct_count[ai - 1] += 1

for c in correct_count:
    if K - Q + c < 1:
        print("No")
    else:
        print("Yes")
