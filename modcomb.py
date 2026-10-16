class ModComb:
    def __init__(self, size: int, mod: int = 998244353):
        self.fact = [1] * (size + 1)
        self.factinv = [1] * (size + 1)
        self.mod = mod

        _fact = self.fact
        _factinv = self.factinv

        for i in range(1, size + 1):
            _fact[i] = _fact[i - 1] * i % mod

        _factinv[size] = pow(_fact[size], -1, mod)
        for i in range(size - 1, -1, -1):
            _factinv[i] = _factinv[i + 1] * (i + 1) % mod

    # nCk
    def comb(self, n: int, k: int) -> int:
        if n < k or k < 0:
            return 0
        return self.fact[n] * self.factinv[k] * self.factinv[n - k] % self.mod

    # nPk
    def perm(self, n: int, k: int) -> int:
        if n < k or k < 0:
            return 0
        return self.fact[n] * self.factinv[n - k] % self.mod
