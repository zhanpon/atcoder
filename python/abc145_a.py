def main():
    a, b = [int(token) for token in input().split()]
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a * b)


if __name__ == '__main__':
    main()
