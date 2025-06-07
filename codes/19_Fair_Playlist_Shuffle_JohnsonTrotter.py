def johnson_trotter(n):
    # Initialize permutation and directions (-1 for left, +1 for right)
    perm = list(range(1, n+1))
    directions = [-1] * n  # all initially moving left
    
    def get_mobile():
        mobile = -1
        mobile_index = -1
        for i in range(n):
            nxt = i + directions[i]
            if 0 <= nxt < n and perm[i] > perm[nxt]:
                if perm[i] > mobile:
                    mobile = perm[i]
                    mobile_index = i
        return mobile_index
    
    result = [perm.copy()]
    
    while True:
        mobile_index = get_mobile()
        if mobile_index == -1:
            break
        
        swap_with = mobile_index + directions[mobile_index]
        perm[mobile_index], perm[swap_with] = perm[swap_with], perm[mobile_index]
        directions[mobile_index], directions[swap_with] = directions[swap_with], directions[mobile_index]
        mobile_index = swap_with
        
        for i in range(n):
            if perm[i] > perm[mobile_index]:
                directions[i] = -directions[i]
        
        result.append(perm.copy())
    
    return result

# Example usage:
if __name__ == "__main__":
    perms = johnson_trotter(3)
    for p in perms:
        print(p)
