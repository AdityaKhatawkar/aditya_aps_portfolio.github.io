# Union-Find (Disjoint Set Union) for User Profiling

class UnionFind:
    def __init__(self, users):
        self.parent = {user: user for user in users}
        self.rank = {user: 0 for user in users}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

    def get_clusters(self):
        clusters = {}
        for user in self.parent:
            root = self.find(user)
            if root not in clusters:
                clusters[root] = []
            clusters[root].append(user)
        return list(clusters.values())

# Example usage
users = ['U1', 'U2', 'U3', 'U4', 'U5', 'U6']
similarity_edges = [('U1', 'U2'), ('U2', 'U3'), ('U4', 'U5')]  # behavioral similarity

uf = UnionFind(users)
for u, v in similarity_edges:
    uf.union(u, v)

clusters = uf.get_clusters()
print("User clusters based on viewing similarity:")
for cluster in clusters:
    print(cluster)
