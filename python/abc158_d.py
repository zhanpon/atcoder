import collections


class Formatter:
    def __init__(self, s):
        self._d = collections.deque(s)
        self._reversed = False

    def reverse(self):
        self._reversed = not self._reversed

    def append(self, s):
        if self._reversed:
            self._d.appendleft(s)
        else:
            self._d.append(s)

    def appendleft(self, s):
        if self._reversed:
            self._d.append(s)
        else:
            self._d.appendleft(s)

    def __iter__(self):
        if self._reversed:
            return reversed(self._d)
        else:
            return iter(self._d)


S = input()
Q = int(input())

d = Formatter(S)

for _ in range(Q):
    Qi = input()
    if Qi == "1":
        d.reverse()
    else:
        T, F, C = Qi.split()
        if F == "1":
            d.appendleft(C)
        else:
            d.append(C)

print("".join(d))
