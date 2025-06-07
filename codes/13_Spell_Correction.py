class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def collect_words(self, node=None, prefix="", results=None):
        if results is None:
            results = []
        if node is None:
            node = self.root
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            self.collect_words(child, prefix + char, results)
        return results

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

def suggest_corrections(trie, word, max_distance=2):
    # Get all words in trie
    candidates = trie.collect_words()
    suggestions = []
    for candidate in candidates:
        dist = levenshtein_distance(word, candidate)
        if dist <= max_distance:
            suggestions.append((candidate, dist))
    # Sort by distance, then alphabetically
    suggestions.sort(key=lambda x: (x[1], x[0]))
    return [s[0] for s in suggestions]

# Example usage
valid_queries = ["cat", "car", "cart", "dog", "dot", "door", "dorm", "apple", "apply"]
trie = Trie()
for q in valid_queries:
    trie.insert(q)

input_word = "dor"  # Misspelled version of "door" or "dorm"
corrections = suggest_corrections(trie, input_word)
print("Did you mean:", corrections)
