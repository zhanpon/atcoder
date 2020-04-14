def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]

    threshold = sum(a) / (4 * m)
    if sum(1 for i in a if i >= threshold) >= m:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
