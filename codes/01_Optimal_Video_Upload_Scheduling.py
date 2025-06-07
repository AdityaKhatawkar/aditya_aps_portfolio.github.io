def optimal_upload_schedule(sizes):
    total = sum(sizes)
    n = len(sizes)
    reachable = {0}
    for s in sizes:
        new_reach = set(reachable)
        for acc in reachable:
            new_reach.add(acc + s)
        reachable = new_reach
    best = max(acc for acc in reachable if acc <= total//2)
    makespan = max(best, total - best)
    return makespan

# Example usage:
sizes = [50, 20, 30, 80, 10]  # chunk sizes (MB or arbitrary units)
print(optimal_upload_schedule(sizes))
