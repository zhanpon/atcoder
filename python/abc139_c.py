import itertools


def count_chains(nums):
    if not nums:
        return

    count = 1
    for m, n in zip(nums, nums[1:]):
        if m >= n:
            count += 1
        else:
            yield count
            count = 1
    yield count


def main():
    n = int(input())
    h = [int(x) for x in input().split()]

    print(max(count_chains(h)) - 1)


if __name__ == "__main__":
    main()
