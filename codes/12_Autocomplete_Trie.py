class Node:
    def __init__(self):
        self.children = [None] * 26
        self.wordEnd = False

def insert(root, key):
    cur = root
    for ch in key:
        index = ord(ch) - ord('a')
        if cur.children[index] is None:
            cur.children[index] = Node()
        cur = cur.children[index]
    cur.wordEnd = True

def search(root, key):
    cur = root
    for ch in key:
        index = ord(ch) - ord('a')
        if cur.children[index] is None:
            return False
        cur = cur.children[index]
    return cur.wordEnd

def main():
    root = Node()
    words = ["apple", "animal", "ball", "baseball", "balling"]
    query = ["banana", "apple", "ball"]

    for word in words:
        insert(root, word)

    for q in query:
        ans = search(root, q)
        print(f"{q} : {ans}")

if __name__ == "__main__":
    main()
