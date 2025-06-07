class KDNode:
    def __init__(self, point, left=None, right=None, axis=0):
        self.point = point  # (lat, lon)
        self.left = left
        self.right = right
        self.axis = axis

def build_kdtree(points, depth=0):
    if not points:
        return None
    k = 2  # 2D points
    axis = depth % k
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    # Create node and subtrees
    return KDNode(
        point=points[median],
        left=build_kdtree(points[:median], depth+1),
        right=build_kdtree(points[median+1:], depth+1),
        axis=axis
    )

def distance_sq(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def nearest_neighbor(root, target, best=None, best_dist=float('inf')):
    if root is None:
        return best, best_dist
    # Check current node
    d = distance_sq(root.point, target)
    if d < best_dist:
        best, best_dist = root.point, d
    # Traverse subtrees
    axis = root.axis
    diff = target[axis] - root.point[axis]
    # Choose side: left if diff<0 else right
    first = root.left if diff < 0 else root.right
    second = root.right if diff < 0 else root.left
    best, best_dist = nearest_neighbor(first, target, best, best_dist)
    # Possibly check opposite side
    if diff**2 < best_dist:
        best, best_dist = nearest_neighbor(second, target, best, best_dist)
    return best, best_dist

# Example usage:
cdn_locations = [(52.5, 13.4), (48.9, 2.4), (40.7, -74.0), (35.7, 139.7)]  # Berlin, Paris, NYC, Tokyo
tree = build_kdtree(cdn_locations)
user_location = (50.0, 8.0)  # Some coordinate
nearest, _ = nearest_neighbor(tree, user_location)
print("Nearest CDN server at:", nearest)
