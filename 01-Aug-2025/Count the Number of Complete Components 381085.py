# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        count = 0
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(n):
            if i not in visited:
                check = set()

                queue = deque()
                queue.append(i)
                check.add(i)
                visited.add(i)
                edge = 0
                while queue:

                   node = queue.popleft()
                   edge += len(graph[node])
                   for nei in graph[node]:
                    
                    if nei not in visited:
                        visited.add(nei)
                        check.add(nei)
                        queue.append(nei)

                

                expected = len(check) * (len(check)-1)
                if edge == expected:
                    count += 1
        return count
                




        