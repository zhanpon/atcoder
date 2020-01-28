def read_line():
    tokens = input().split()
    p = int(tokens[0])
    S = tokens[1]
    return p, S

N, M = map(int, input().split())

wa_counters = [0 for _ in range(N + 1)]
correct_answers = 0
penalties = 0
for _ in range(M):
    p, S = read_line()
    if wa_counters[p] == -1:
        continue

    if S == "AC":
        penalties += wa_counters[p]
        correct_answers += 1
        wa_counters[p] = -1
    else:
        wa_counters[p] += 1

print(correct_answers, penalties)
