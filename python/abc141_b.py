def good(i, s):
    if i % 2 == 1:
        return s in ["R", "U", "D"]
    else:
        return s in ["L", "U", "D"]


S = input()

if all(good(i, s) for i, s in enumerate(S, 1)):
    print("Yes")
else:
    print("No")
