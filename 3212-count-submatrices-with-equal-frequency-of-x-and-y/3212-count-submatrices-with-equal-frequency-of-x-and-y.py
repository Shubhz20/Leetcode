from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # prefix sums
        px = [[0]*n for _ in range(m)]
        py = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # current cell
                if grid[i][j] == 'X':
                    px[i][j] = 1
                elif grid[i][j] == 'Y':
                    py[i][j] = 1
                
                # add top
                if i > 0:
                    px[i][j] += px[i-1][j]
                    py[i][j] += py[i-1][j]
                
                # add left
                if j > 0:
                    px[i][j] += px[i][j-1]
                    py[i][j] += py[i][j-1]
                
                # remove double count
                if i > 0 and j > 0:
                    px[i][j] -= px[i-1][j-1]
                    py[i][j] -= py[i-1][j-1]
        
        # count valid submatrices
        count = 0
        
        for i in range(m):
            for j in range(n):
                if px[i][j] == py[i][j] and px[i][j] > 0:
                    count += 1
        
        return count