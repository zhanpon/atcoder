from collections import Counter

S = input()

if list(Counter(S).values()) == [2, 2]:
    print("Yes")
else:
    print("No")
