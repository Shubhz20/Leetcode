from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        # if total is odd → impossible
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # ----- Check horizontal cuts -----
        curr = 0
        for i in range(m - 1):  # ensure bottom part is non-empty
            curr += sum(grid[i])
            if curr == target:
                return True
        
        # ----- Check vertical cuts -----
        col_sums = [0] * n
        for j in range(n):
            for i in range(m):
                col_sums[j] += grid[i][j]
        
        curr = 0
        for j in range(n - 1):  # ensure right part is non-empty
            curr += col_sums[j]
            if curr == target:
                return True
        
        return False