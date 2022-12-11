from collections import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(i, j, grid)
        return cnt
    
    def dfs(self, i, j, grid):#helper: depth first search
        #reach to the edge
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"#avoid go back and become infinite loop
        self.dfs(i-1, j, grid)
        self.dfs(i+1, j, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i, j+1, grid)
        return
    #time complexity: O(MN)
    #space complexity: O(MN)