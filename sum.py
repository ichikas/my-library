class Cumulative_Sum_2D:
    def __init__(self, arr, h, w):
        self.dat = [[0] * (w + 1) for _ in range(h + 1)]

        for x in range(h):
            for y in range(w):
                self.dat[x + 1][y + 1] = self.dat[x + 1][y] + arr[x][y]

        for y in range(w):
            for x in range(h):
                self.dat[x + 1][y + 1] = self.dat[x + 1][y + 1] + self.dat[x][y + 1]

    # 左上(a, b), 右下(c, d)
    def get_sum(self, a, b, c, d):
        return (
            self.dat[a][b]
            + self.dat[c + 1][d + 1]
            - self.dat[a][d + 1]
            - self.dat[c + 1][b]
        )
