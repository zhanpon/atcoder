N = int(input())
B = [int(x) for x in input().split()]

s = B[0] + B[-1]
for i in range(N - 2):
    s += min(B[i], B[i + 1])

print(s)
