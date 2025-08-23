# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        d = ([1,1], [-1, - 1], [1, -1], [-1, 1], [0,1],[0,-1],[-1,0], [1,0])
        queue = deque()
        queue.append([click[0], click[1]])
        visited = {(click[0], click[1])}


        def isValid(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0]) and (x,y) not in visited

        while queue:
            i, j = queue.popleft()
          

            if board[i][j] == 'M':
                board[i][j] = 'X'
                return board
            c = 0
            nei = []

            for dx, dy in d:
                ni = i + dx
                nj = j + dy
                if isValid(ni, nj):
                     
                    nei.append([ni,nj])
                    if board[ni][nj] == "M":
                        c += 1
                    
            if not c:
                board[i][j] = 'B'
                for ni, nj in nei:
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        queue.append((ni, nj))
            else:
                board[i][j] = str(c)
        
        return board