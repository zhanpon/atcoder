N, A, B = map(int, input().split())

div, mod = divmod(N, A + B)
print(A * div + min(A, mod))
