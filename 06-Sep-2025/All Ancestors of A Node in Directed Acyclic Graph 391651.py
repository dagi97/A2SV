# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ans = [set() for _ in range(n)]
        indegree = [0 for i in range(n)]
        queue = deque()
        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1
        for i in range(n):
            if not indegree[i]:
                queue.append(i)
        
        while queue:
            i = queue.popleft()
            for nei in graph[i]:
                ans[nei].add(i)
                ans[nei].update(ans[i])
                indegree[nei] -= 1
                if not indegree[nei]:
                    queue.append(nei)
            ans[i] = sorted(ans[i])
        return ans
                
        

        

       

            
        