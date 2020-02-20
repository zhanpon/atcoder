N, D = map(int, input().split())

div, mod = divmod(N, 2 * D + 1)
if mod == 0:
    print(div)
else:
    print(div + 1)
