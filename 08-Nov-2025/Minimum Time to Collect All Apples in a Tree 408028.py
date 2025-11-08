# Problem: Minimum Time to Collect All Apples in a Tree - https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
      

        def dfs(n):
            
            visited.add(n)

            ans = sum(dfs(nei) for nei in graph[n] if nei not in visited)
              
            if not hasApple[n] and not ans:
                return 0
            return ans + 2
        return max(0, dfs(0)-2)

      
        
        