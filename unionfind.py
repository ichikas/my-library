class UnionFind:
    def __init__(self, n):
        self.N = n
        self.par = [-1] * n
        self.siz = [1] * n
        self.cnt = n

    def root(self, x):
        p = self.par
        if p[x] == -1:
            return x

        r = x
        while p[r] != -1:
            r = p[r]
        while x != r:
            nex = p[x]
            p[x] = r
            x = nex
        return r

    def unite(self, u, v):
        r_u = self.root(u)
        r_v = self.root(v)
        if r_u == r_v:
            return False

        self.cnt -= 1
        p = self.par
        s = self.siz
        if s[r_u] > s[r_v]:
            r_u, r_v = r_v, r_u
        p[r_u] = r_v
        s[r_v] += s[r_u]
        return True

    def same(self, u, v):
        return self.root(u) == self.root(v)

    def size(self, x):
        return self.siz[self.root(x)]

    def group_num(self):
        return self.cnt
