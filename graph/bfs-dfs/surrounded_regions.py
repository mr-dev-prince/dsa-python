from typing import List

class Solution:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def dfs(self, board, r, c, vis):
        vis[r][c] = 1
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and not vis[nr][nc] and board[nr][nc] == 'O':
                self.dfs(board, nr, nc, vis)
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        vis = [[0] * col for _ in range(row)]

        # first and last row
        for c in range(col):
            if not vis[0][c] and board[0][c] == "O":
                self.dfs(board, 0, c, vis)
            
            if not vis[row - 1][c] and board[row - 1][c] == "O":
                self.dfs(board, row - 1, c, vis)

        # first and last column
        for r in range(row):
            if not vis[r][0] and board[r][0] == "O":
                self.dfs(board, r, 0, vis)
            
            if not vis[r][col - 1] and board[r][col - 1] == "O":
                self.dfs(board, r, col - 1, vis)

        for i in range(row):
            for j in range(col):
                if not vis[i][j]:
                    board[i][j] = "X"
