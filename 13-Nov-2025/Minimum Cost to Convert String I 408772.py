# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        check = [[float('inf')] * 26 for _ in range(26)]
        n = len(cost)
        for i in range(26):
            check[i][i] = 0
       

        for i in range(n):
            a = ord(original[i]) - 97
            b = ord(changed[i]) - 97
            check[a][b] = min(cost[i], check[a][b])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if check[i][j] > check[i][k] + check[k][j]:
                        check[i][j] =  check[i][k] + check[k][j]

        ans = 0
        for i in range(len(target)):

            if source[i] != target[i]:
                if  check[ord(source[i]) - 97][ord(target[i]) - 97] == float('inf'):
                    return -1
                else:
                    ans +=  check[ord(source[i]) - 97][ord(target[i]) - 97]
        return ans
            

                


        
      
        


        