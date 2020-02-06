N = int(input())
A = [int(s) for s in input().split()]

acc = 0.0
for a in A:
    acc += 1 / a

print(1 / acc)
