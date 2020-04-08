import collections

ORD_A = ord("a")


def count_chars(s):
    counter = [0 for _ in range(26)]
    for c in s:
        counter[ord(c) - ORD_A] += 1

    return counter


def main():
    n = int(input())
    anagram_counter = collections.Counter(tuple(count_chars(input())) for _ in range(n))

    combinations_times_2 = sum(v * (v - 1) for v in anagram_counter.values())
    print(combinations_times_2 // 2)


if __name__ == "__main__":
    main()
