# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        c =  0
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                check = {i}
                queue = deque()
                queue.append(i)
                edges = 0
                while queue:
                    a = queue.popleft()
                    edges += len(graph[a])

                    for nei in graph[a]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                            check.add(nei)
                expected = len(check) * (len(check) - 1)
                if expected == edges:
                    c += 1

        return c 





        
        
        
        
       