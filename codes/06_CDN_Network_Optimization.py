def boruvka_mst(nodes, edges):
    parent = {u: u for u in nodes}
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    def union(u,v):
        parent[find(u)] = find(v)
    mst = []
    num_components = len(nodes)
    # Continue until one component
    while num_components > 1:
        cheapest = {u: None for u in nodes}
        # For each edge, see if it is cheapest for its component
        for u,v,w in edges:
            ru, rv = find(u), find(v)
            if ru == rv: continue
            # Check for component ru
            if cheapest[ru] is None or cheapest[ru][2] > w:
                cheapest[ru] = (u,v,w)
            # Check for component rv
            if cheapest[rv] is None or cheapest[rv][2] > w:
                cheapest[rv] = (u,v,w)
        # Add cheapest edges
        for comp, edge in cheapest.items():
            if edge:
                u,v,w = edge
                if find(u) != find(v):
                    union(u,v)
                    mst.append((u,v,w))
                    num_components -= 1
    return mst

# Example:
nodes = ['A','B','C','D']
edges = [
    ('A','B',3), ('B','C',1), ('A','C',4),
    ('C','D',2), ('B','D',5)
]
print(boruvka_mst(nodes, edges))
