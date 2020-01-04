a, b, k = [int(x) for x in input().split()]

if k <= a:
    print(a - k, b)
elif k <= a + b:
    print(0, a + b - k)
else:
    print(0, 0)
