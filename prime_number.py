n = int(input())

is_prime = [True] * (n + 1)
is_prime[0], is_prime[1] = False, False
prime_nums = []
min_factor = [-1] * (n + 1)
for x in range(2, n + 1):
    if not is_prime[x]:
        continue

    prime_nums.append(x)
    min_factor[x] = x
    for y in range(x * x, n + 1, x):
        is_prime[y] = False
        if min_factor[y] == -1:
            min_factor[y] = x


def modinv(a: int, m: int):
    a_, m_ = a, m
    x, y = 1, 0
    nx, ny = 0, 1

    while m:
        q = a // m
        a, m = m, a % m
        x, nx = nx, x - q * nx
        y, ny = ny, y - q * ny

    if a != 1:
        return None

    return x % m_
