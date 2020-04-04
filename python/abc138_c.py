import functools


def new_ingredient(x, y):
    return (x + y) / 2


def main():
    n = int(input())
    v = [int(x) for x in input().split()]

    v.sort()
    max_value = functools.reduce(new_ingredient, v)

    print(max_value)


if __name__ == "__main__":
    main()
