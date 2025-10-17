# Problem: Replace Words - https://leetcode.com/problems/replace-words/


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
    
        for i in range (len(word)):
            if node.is_end:
                return word[:i]
            if node.children[ord(word[i])- 97] is None:
                return word
            print(node.is_end,word[i])
            if node.is_end:
                return node
               
            node =  node.children[ord(word[i])- 97]
          

        return word
            
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for root in dictionary:
            trie.insert(root)
        s = sentence.split(' ')
        for i in range(len(s)):
            s[i] = trie.search(s[i])
        return ' '.join(s)

        
        