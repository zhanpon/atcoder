S = input()
T = input()

n = sum(1 for s, t in zip(S, T) if s == t)
print(n)
