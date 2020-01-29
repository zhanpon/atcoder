H, A = map(int, input().split())

div, mod = divmod(H, A)

if mod == 0:
    print(div)
else:
    print(div + 1)
