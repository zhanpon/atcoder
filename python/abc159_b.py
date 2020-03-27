def is_palindrome(s):
    return all(c1 == c2 for c1, c2 in zip(s, reversed(s)))


S = input()
N = len(S)

if all(is_palindrome(s) for s in (S, S[: (N - 1) // 2], S[(N + 3) // 2 - 1 :])):
    print("Yes")
else:
    print("No")
