def rabin_karp_fingerprint_scan(stream, known_hashes, base=256, mod=10**9+7, window_size=10):

    n = len(stream)
    if n < window_size:
        return []

    result = []
    # Precompute base^(window_size-1)
    h = pow(base, window_size - 1, mod)

    # Compute hash for the first window
    current_hash = 0
    for i in range(window_size):
        current_hash = (current_hash * base + ord(stream[i])) % mod

    # Store hashes of known copyrighted sequences
    known_set = set(known_hashes)

    # Compare initial window
    if current_hash in known_set:
        result.append(0)

    # Slide the window
    for i in range(1, n - window_size + 1):
        # Remove leftmost char and add rightmost char
        current_hash = (current_hash - ord(stream[i - 1]) * h) % mod
        current_hash = (current_hash * base + ord(stream[i + window_size - 1])) % mod
        current_hash = (current_hash + mod) % mod  # Handle negative mod

        if current_hash in known_set:
            result.append(i)

    return result


if __name__ == "__main__":
    # Simulated incoming data chunk
    incoming_data = "abcdefghijxyzcopiedcontenthere"

    # Simulated known copyright hashes (pretend precomputed)
    def compute_hash(text, base=256, mod=10**9+7):
        h = 0
        for c in text:
            h = (h * base + ord(c)) % mod
        return h

    known_copyrights = [
        "copiedconte",  # window size = 10
        "piratedsegm"
    ]

    known_hashes = [compute_hash(x) for x in known_copyrights]

    matches = rabin_karp_fingerprint_scan(incoming_data, known_hashes)

    print("Potential Copyright Match Indices:", matches)
