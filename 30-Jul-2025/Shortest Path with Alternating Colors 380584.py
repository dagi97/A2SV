# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        red = defaultdict(list)
        blue = defaultdict(list)


        for u,v in redEdges:
            red[u].append(v)
          
        
        for u,v in blueEdges:
            blue[u].append(v)
          

        ans = [-1] * n

        queue = deque()
        queue.append([0,0,None])
        
        visited = set((0,None))
        

        while queue:
            n, length , color = queue.popleft()

            if ans[n] == -1:
                ans[n] = length
            if color != "RED":
                for nei in red[n]:
                    if (nei,"RED") not in visited:
                        visited.add((nei,"RED"))
                        queue.append([nei,length + 1, "RED"])

            if color != "BLUE":
                 for nei in  blue[n]:
                    if (nei,"BLUE") not in visited:
                        visited.add((nei,"BLUE"))
                        queue.append([nei,length + 1, "BLUE"])
        return ans


        

        