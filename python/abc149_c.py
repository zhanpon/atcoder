def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def smallest_prime_above_n(n: int) -> int:
    prime_candidate = n
    while True:
        if is_prime(prime_candidate):
            return prime_candidate
        prime_candidate += 1


X = int(input())
print(smallest_prime_above_n(X))
