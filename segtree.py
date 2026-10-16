def op(a, b):
    return a + b


ide_ele = 0


class SegTree:
    def __init__(self, List, operation=op, identity_element=ide_ele):
        n_ = len(List)
        op_ = operation
        e_ = identity_element
        siz_ = 1 << (n_ - 1).bit_length()
        dat = [e_] * (siz_ << 1)

        dat[siz_ : siz_ + n_] = List

        for i in range(siz_ - 1, 0, -1):
            l = i << 1
            dat[i] = op_(dat[l], dat[l | 1])

        self._op = op_
        self._e = e_
        self._siz = siz_
        self._dat = dat

    def set(self, p, x):
        dat = self._dat
        op_ = self._op
        p += self._siz
        dat[p] = x
        while p > 1:
            p >>= 1
            l = p << 1
            dat[p] = op_(dat[l], dat[l | 1])

    def add(self, p, x):
        dat = self._dat
        op_ = self._op
        p += self._siz
        dat[p] += x
        while p > 1:
            p >>= 1
            l = p << 1
            dat[p] = op_(dat[l], dat[l | 1])

    def get(self, p):
        return self._dat[p + self._siz]

    def prod(self, l, r):
        dat = self._dat
        op_ = self._op
        l += self._siz
        r += self._siz
        res = self._e
        while l < r:
            if l & 1:
                res = op_(res, dat[l])
                l += 1
            if r & 1:
                r -= 1
                res = op_(res, dat[r])
            l >>= 1
            r >>= 1
        return res
