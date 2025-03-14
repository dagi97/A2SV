# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        self.l = 0
        nums = list([i for i in range(1,n+1)])
        def game(n,k):
            if len(n) == 1:
                return n[0]
            self.l = (self.l+k-1) % len(n)
            n.pop(self.l)

            return game(n,k)
            
        return game(nums,k)
            


