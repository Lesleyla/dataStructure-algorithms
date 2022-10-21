from collections import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wordList = list(word)
        for i in range(m):
            for j in range(n):
                if self.dfs(board, wordList, i, j):
                    return True
        return False
    def dfs(self, board, wordList, i, j):
        if not wordList:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != wordList[0]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"
        res = self.dfs(board, wordList[1:], i + 1, j) or self.dfs(board, wordList[1:], i - 1, j) or self.dfs(board, wordList[1:], i, j + 1) or self.dfs(board, wordList[1:], i, j - 1)
        board[i][j] = tmp
        return res