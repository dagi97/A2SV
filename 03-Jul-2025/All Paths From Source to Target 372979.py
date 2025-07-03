# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
     
        ans = []
        
        def dfs(i, path):
            path.append(i)

            if i == len(graph) - 1:
                ans.append(path[:])
                return

            for n in graph[i]:
                 dfs(n, path)
                 path.pop()
                      
        dfs(0, [])
        

            
        return ans