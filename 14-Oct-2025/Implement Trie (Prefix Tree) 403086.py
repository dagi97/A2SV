# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False
class Trie:

    def __init__(self):
         
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.children[ord(char)- 97] is None:
                node.children[ord(char)- 97]= TrieNode()
            node =  node.children[ord(char)- 97]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.children[ord(char)- 97] is None:
                return False
            node =  node.children[ord(char)- 97]
        return node.is_end
            

        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node.children[ord(char)- 97] is None:
                return False
            node =  node.children[ord(char)- 97]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)