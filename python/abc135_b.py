def swap_ij(xs, i, j):
    xs[i], xs[j] = xs[j], xs[i]


def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    sorted_p = sorted(p)

    for i in range(N):
        for j in range(i, N):
            swap_ij(p, i, j)
            if p == sorted_p:
                print("YES")
                return
            else:
                swap_ij(p, i, j)

    print("NO")


if __name__ == "__main__":
    main()
