# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False

    def addWord(self, word: str) -> None:

        node = self

        for char in word:
            if node.children[ord(char)- 97] is None:
                node.children[ord(char)- 97] = WordDictionary()
            node =  node.children[ord(char)- 97]
        node.is_end = True

        

    def search(self, word: str) -> bool:
        return self.help(word, 0)

    def help(self, word: str, ind:int) -> bool:

        if ind == len(word):
            return self.is_end
       
        if word[ind] == '.':
            for child in self.children:
                if child and child.help(word, ind + 1):
                    return True
            return False
        
        else:
            if self.children[ord(word[ind]) - 97] is None:
                  return False
            return self.children[ord(word[ind]) - 97].help(word, ind + 1)

 
     

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)