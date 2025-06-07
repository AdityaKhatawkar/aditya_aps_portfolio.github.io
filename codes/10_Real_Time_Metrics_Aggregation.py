class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.ft = [0]*(n+1)
    def update(self, i, delta):
        while i <= self.n:
            self.ft[i] += delta
            i += i & -i
    def query(self, i):
        s = 0
        while i > 0:
            s += self.ft[i]
            i -= i & -i
        return s
    def range_query(self, L, R):
        return self.query(R) - self.query(L-1)

# Example usage (1-indexed days):
views = FenwickTree(7)
# e.g., day1 got 100 views, day3 got 50
views.update(1, 100)
views.update(3, 50)
print(views.range_query(1, 3))  # 150
