import heapq

def a_star(start, goal, neighbors_fn, heuristic):
    open_set = [(0 + heuristic(start, goal), 0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    while open_set:
        est_total, cost, current = heapq.heappop(open_set)
        if current == goal:
            break
        for nxt, w in neighbors_fn(current):
            new_cost = cost + w
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + heuristic(nxt, goal)
                heapq.heappush(open_set, (priority, new_cost, nxt))
                came_from[nxt] = current
    # Reconstruct path
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from.get(cur, start)
    path.append(start)
    path.reverse()
    return path, cost_so_far.get(goal, float('inf'))

# Example: grid neighbors function
def grid_neighbors(pos):
    x,y = pos
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nxt = (x+dx,y+dy)
        yield nxt, 1  # unit weight

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

path, dist = a_star((0,0), (5,5), grid_neighbors, manhattan)
print(path, dist)
