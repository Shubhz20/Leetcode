from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
                sums.add(grid[r][c])   # size 0 rhombus
                
                k = 1
                while True:
                    if r + 2*k >= m or c - k < 0 or c + k >= n:
                        break
                    
                    total = 0
                    
                    # top -> right
                    i, j = r, c
                    for _ in range(k):
                        total += grid[i][j]
                        i += 1
                        j += 1
                    
                    # right -> bottom
                    for _ in range(k):
                        total += grid[i][j]
                        i += 1
                        j -= 1
                    
                    # bottom -> left
                    for _ in range(k):
                        total += grid[i][j]
                        i -= 1
                        j -= 1
                    
                    # left -> top
                    for _ in range(k):
                        total += grid[i][j]
                        i -= 1
                        j += 1
                    
                    sums.add(total)
                    k += 1
        
        return sorted(sums, reverse=True)[:3]