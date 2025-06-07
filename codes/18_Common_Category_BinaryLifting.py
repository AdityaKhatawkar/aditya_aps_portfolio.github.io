import sys
sys.setrecursionlimit(10**7)

class BinaryLiftingLCA:
    def __init__(self, n, edges, root=0):
        self.n = n
        self.LOG = (n-1).bit_length()
        self.adj = [[] for _ in range(n)]
        for u,v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.depth = [0]*n
        self.parent = [[-1]*n for _ in range(self.LOG)]
        self.root = root
        self.dfs(root, -1, 0)
        self.preprocess()

    def dfs(self, node, par, d):
        self.parent[0][node] = par
        self.depth[node] = d
        for nxt in self.adj[node]:
            if nxt != par:
                self.dfs(nxt, node, d+1)

    def preprocess(self):
        for i in range(1, self.LOG):
            for v in range(self.n):
                if self.parent[i-1][v] != -1:
                    self.parent[i][v] = self.parent[i-1][self.parent[i-1][v]]

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        # Lift u up to same depth as v
        diff = self.depth[u] - self.depth[v]
        for i in range(self.LOG):
            if diff & (1 << i):
                u = self.parent[i][u]

        if u == v:
            return u

        # Lift both until parents differ
        for i in reversed(range(self.LOG)):
            if self.parent[i][u] != self.parent[i][v]:
                u = self.parent[i][u]
                v = self.parent[i][v]

        return self.parent[0][u]

# Example usage:
if __name__ == "__main__":
    # Tree edges (0-based indexing)
    edges = [
        (0,1), (0,2), (1,3), (1,4), (2,5), (2,6)
    ]
    n = 7
    lca_solver = BinaryLiftingLCA(n, edges, root=0)

    # Query LCA of nodes 3 and 4
    print("LCA of 3 and 4:", lca_solver.lca(3, 4))  # Output: 1
    # Query LCA of nodes 4 and 6
    print("LCA of 4 and 6:", lca_solver.lca(4, 6))  # Output: 0
