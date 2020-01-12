N = int(input())
S = input()

count = sum(1 for i in range(N - 2) if S[i:i + 3] == "ABC")
print(count)
