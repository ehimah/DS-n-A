class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWordEnd = True

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isWordEnd


def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", t.search("the")))
    print("{} ---- {}".format("these", t.search("these")))
    print("{} ---- {}".format("their", t.search("their")))
    print("{} ---- {}".format("thaw", t.search("thaw")))


if __name__ == '__main__':
    main()
