# 17_Video_Importance_PageRank.py

import numpy as np

def pagerank(adj_matrix, damping=0.85, max_iter=100, tol=1e-6):
    n = adj_matrix.shape[0]
    # Normalize adjacency matrix to column stochastic
    col_sums = adj_matrix.sum(axis=0)
    stochastic_matrix = adj_matrix / col_sums[np.newaxis, :]
    stochastic_matrix = np.nan_to_num(stochastic_matrix)  # handle division by zero

    rank = np.ones(n) / n
    for _ in range(max_iter):
        prev_rank = rank.copy()
        rank = (1 - damping) / n + damping * stochastic_matrix @ rank
        if np.linalg.norm(rank - prev_rank, 1) < tol:
            break
    return rank

# Example graph adjacency matrix (edges represent video transitions)
# Rows: source video, Columns: destination video
adj = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
], dtype=float)

ranks = pagerank(adj)
print("PageRank scores:", ranks)
