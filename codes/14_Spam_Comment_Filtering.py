import hashlib

class BloomFilter:
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, word):
        result = []
        for i in range(self.hash_count):
            hash_input = word + str(i)
            hash_val = int(hashlib.sha256(hash_input.encode()).hexdigest(), 16)
            result.append(hash_val % self.size)
        return result

    def add(self, word):
        for h in self._hashes(word):
            self.bit_array[h] = 1

    def check(self, word):
        return all(self.bit_array[h] == 1 for h in self._hashes(word))


# Example usage
banned_phrases = ["buy now", "free money", "click here", "subscribe now"]
comments = [
    "You should click here to win a prize!",
    "Great video!",
    "Don't miss out on free money!",
    "This was informative and well explained."
]

# Initialize Bloom Filter
bloom = BloomFilter()

# Add banned phrases
for phrase in banned_phrases:
    bloom.add(phrase.lower())

# Check comments
for comment in comments:
    flagged = any(bloom.check(phrase) for phrase in comment.lower().split())
    status = "🚫 Flagged as Spam" if flagged else "✅ Safe"
    print(f"Comment: {comment}\nStatus: {status}\n")
