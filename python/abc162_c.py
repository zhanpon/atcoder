import math
from functools import lru_cache
from itertools import combinations


@lru_cache(maxsize=None)
def gcd2(a: int, b: int) -> int:
    return math.gcd(a, b)


def gcd3(a: int, b: int, c: int) -> int:
    return gcd2(gcd2(a, b), c)


def main() -> None:
    k = int(input())

    one_to_k = range(1, k + 1)
    s1 = sum(one_to_k)
    s2 = sum(gcd2(a, b) for a, b in combinations(one_to_k, 2))
    s3 = sum(gcd3(a, b, c) for a, b, c in combinations(one_to_k, 3))
    print(s1 + 6 * s2 + 6 * s3)


if __name__ == "__main__":
    main()
