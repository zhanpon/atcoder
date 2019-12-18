n = int(input())
if n in {a * b for a in range(1, 10) for b in range(1, 10)}:
    print("Yes")
else:
    print("No")
