def knapsack_max_quality(sizes, qualities, W):
    n = len(sizes)
    # dp[w] = max quality for bandwidth w
    dp = [0] * (W+1)
    for i in range(n):
        sz, q = sizes[i], qualities[i]
        # Traverse weights backward to avoid reuse
        for w in range(W, sz-1, -1):
            dp[w] = max(dp[w], dp[w-sz] + q)
    return dp[W]

# Example usage: 3 segments with sizes and quality scores
sizes = [2, 3, 4]       # bandwidth units
qualities = [3, 4, 5]   # arbitrary quality values
bandwidth_budget = 5
print("Max quality:", knapsack_max_quality(sizes, qualities, bandwidth_budget))
