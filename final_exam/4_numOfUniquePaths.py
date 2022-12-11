# current paths = top_paths + left_paths
# but if we have block at that location then we need to set it to 0 in order to block path from top and left

from collections import List
#find number of unique paths with obstacles
def numOfUniquePaths(self, obstacleGrid: List[List[int]]) -> int:
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    obstacleGrid[0][0] = 1
    memo = [[0]*cols for _ in range(rows)]
    #corner case: if start point is blocked then no path
    if obstacleGrid[0][0] == 1:
        return 0    
    else:
        memo[0][0] = 1
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue
            if obstacleGrid[i][j] != 1:
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
    return memo[-1][-1]
    
#time complexity: O(N**2) [iterate over the 2D matrix]
#space complexity: O(N**2) [use extra grid memo]