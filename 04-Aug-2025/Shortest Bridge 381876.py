# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = [[False]*n for _ in range(n)]
        queue = deque()

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1 or visited[i][j]:
                return
            visited[i][j] = True
            grid[i][j] = 2
            queue.append((i, j))
            for dx, dy in directions:
                dfs(i + dx, j + dy)

        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if grid[nx][ny] == 1:
                            return steps
                        elif grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            steps += 1

        return -1
