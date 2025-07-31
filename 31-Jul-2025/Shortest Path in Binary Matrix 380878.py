# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        d = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1)]
        visited = set()
        n = len(grid)
       
        def isValid(x, y):
            return (x,y) not in visited and 0 <= x < n and 0 <= y < n and grid[x][y] == 0

                
    
        queue = deque()
        queue.append([0,0])
        visited.add((0,0))
        path = 1
        
        while queue:
            for _ in range(len(queue)):
                a, b = queue.popleft()
                if a == n - 1 and b == n - 1:
                    return path
               
                for dx, dy in d:
                    nr, nc = a + dx, b + dy  
                    if isValid(nr, nc): 
                        visited.add((nr,nc))
                        queue.append((nr, nc))
            path += 1
                 
                
                       
                
        return -1


         
 
   
        