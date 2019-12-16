def price(a: int, b: int, n: int) -> int:
    return a * n + b * len(str(n))


def main():
    a, b, x = [int(token) for token in input().split()]

    if price(a, b, 1) > x:
        print(0)
        return

    if price(a, b, 10 ** 9) < x:
        print(10 ** 9)
        return

    lower_bound = 0
    upper_bound = 10 ** 9
    while upper_bound - lower_bound > 1:
        sample = (upper_bound + lower_bound) // 2
        val = price(a, b, sample)
        if val == x:
            print(sample)
            return
        elif val < x:
            lower_bound = sample
        else:
            upper_bound = sample

    print(lower_bound)


if __name__ == '__main__':
    main()
