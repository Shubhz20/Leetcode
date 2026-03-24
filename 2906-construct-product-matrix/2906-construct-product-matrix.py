from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        # Step 1: Flatten grid
        arr = []
        for row in grid:
            for val in row:
                arr.append(val % MOD)
        
        size = len(arr)
        
        # Step 2: Prefix
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        # Step 3: Suffix
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        # Step 4: Result
        result = [(prefix[i] * suffix[i]) % MOD for i in range(size)]
        
        # Step 5: Convert back to 2D
        ans = []
        idx = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(result[idx])
                idx += 1
            ans.append(row)
        
        return ans 