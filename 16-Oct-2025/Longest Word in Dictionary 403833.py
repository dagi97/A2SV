# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if node.children[ord(char)-97] is None:
                node.children[ord(char)-97] = TrieNode()
            node = node.children[ord(char)-97]
        node.is_end = True
    def search(self, word):
        node = self.root
        for char in word:
            if node.children[ord(char)-97] is None:
                return False
            node = node.children[ord(char)-97]
        return node.is_end
  
    
class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie = Trie()
        ans = ""

        for char in words:
            trie.insert(char)

        for char in words:
            valid = True
            for i in range(1, len(char)):
                if not trie.search( char[:i]):
                    valid = False
                    break
            if valid and len(char) >= len(ans):
                if len(char) > len(ans) or char < ans:
                    ans = char 
             
        
         
            
        return ans




       

        