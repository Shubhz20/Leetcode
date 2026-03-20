from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        ans = []
        
        for i in range(m - k + 1):
            row_ans = []
            for j in range(n - k + 1):
                
                vals = []
                
                # collect k x k elements
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                
                # keep only distinct values
                vals = sorted(set(vals))
                
                # if only one unique value
                if len(vals) <= 1:
                    row_ans.append(0)
                    continue
                
                min_diff = float('inf')
                
                for t in range(len(vals) - 1):
                    min_diff = min(min_diff, vals[t+1] - vals[t])
                
                row_ans.append(min_diff)
            
            ans.append(row_ans)
        
        return ans