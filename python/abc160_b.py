X = int(input())

num_500, mod = divmod(X, 500)
num_5 = mod // 5

print(1000 * num_500 + 5 * num_5)
