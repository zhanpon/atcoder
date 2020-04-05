import collections


def main():
    h, w = read_ints()
    sy, sx = [n - 1 for n in read_ints()]
    gy, gx = [n - 1 for n in read_ints()]
    c = [list(input()) for _ in range(h)]

    c[sy][sx] = 0

    queue = collections.deque([(sy, sx)])
    while queue:
        i, j = queue.popleft()
        for di, dj in (0, -1), (0, 1), (-1, 0), (1, 0):
            k, l = i + di, j + dj
            if c[k][l] == ".":
                c[k][l] = c[i][j] + 1
                queue.append((k, l))

    print(c[gy][gx])


def read_ints():
    return map(int, input().split())


if __name__ == "__main__":
    main()
