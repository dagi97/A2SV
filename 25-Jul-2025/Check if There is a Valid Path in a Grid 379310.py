# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up = {x: set([2,3,4]) for x in [2,5,6]}
        down =  {x: set([2,5,6]) for x in [2,3,4]}
        left =  {x: set([1,4,6]) for x in [1,3,5]}
        right =  {x: set([1,3,5]) for x in [1,4,6]}

        queue = deque([(0,0)])
        directions = [(1,0,down),(0,1,right),(-1,0,up),(0,-1,left)]
        visited = set((0,0))

        def inbound(x,y, d,i,j):
            return 0 <= x < len(grid) and 0 <= y  < len(grid[0]) and (x,y) not in visited and grid[i][j] in d and grid[x][y] in d[ grid[i][j]]



        while queue:
            i, j = queue.popleft()

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                 return True 
            for dx, dy , k in directions:
                x, y = i + dx, j + dy
               
                if inbound(x, y , k ,i ,j):
                    visited.add((x,y))
                    queue.append((x,y))
        return False

    
