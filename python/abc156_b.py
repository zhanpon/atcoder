N, K = map(int, input().split())

i = 0
while True:
    if K ** i > N:
        break
    i += 1

print(i)
