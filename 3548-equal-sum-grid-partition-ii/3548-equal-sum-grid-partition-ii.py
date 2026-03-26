from typing import List
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        # ---------- SINGLE ROW ----------
        if m == 1:
            arr = grid[0]
            left_sum = 0
            
            for j in range(n - 1):
                left_sum += arr[j]
                right_sum = total - left_sum
                
                if left_sum == right_sum:
                    return True
                
                diff = abs(left_sum - right_sum)
                
                if left_sum > right_sum:
                    if arr[0] == diff or arr[j] == diff:
                        return True
                else:
                    if arr[j+1] == diff or arr[-1] == diff:
                        return True
            
            return False

        # ---------- SINGLE COLUMN ----------
        if n == 1:
            arr = [grid[i][0] for i in range(m)]
            top_sum = 0
            
            for i in range(m - 1):
                top_sum += arr[i]
                bottom_sum = total - top_sum
                
                if top_sum == bottom_sum:
                    return True
                
                diff = abs(top_sum - bottom_sum)
                
                if top_sum > bottom_sum:
                    if arr[0] == diff or arr[i] == diff:
                        return True
                else:
                    if arr[i+1] == diff or arr[-1] == diff:
                        return True
            
            return False

        # ---------- GENERAL CASE ----------

        # Horizontal cuts
        top_counter = Counter()
        bottom_counter = Counter()
        for row in grid:
            bottom_counter.update(row)

        top_sum = 0

        for i in range(m - 1):
            for v in grid[i]:
                top_counter[v] += 1
                bottom_counter[v] -= 1
                if bottom_counter[v] == 0:
                    del bottom_counter[v]

            top_sum += sum(grid[i])
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            # ----- FIXED PART -----
            if top_sum > bottom_sum:
                rows = i + 1
                if rows == 1:
                    row = grid[0]
                    if row[0] == diff or row[-1] == diff:
                        return True
                else:
                    if diff in top_counter:
                        return True
            else:
                rows = m - i - 1
                if rows == 1:
                    row = grid[i+1]
                    if row[0] == diff or row[-1] == diff:
                        return True
                else:
                    if diff in bottom_counter:
                        return True

        # Vertical cuts
        left_counter = Counter()
        right_counter = Counter()

        for j in range(n):
            for i in range(m):
                right_counter[grid[i][j]] += 1

        left_sum = 0

        for j in range(n - 1):
            col_sum = 0
            for i in range(m):
                v = grid[i][j]
                col_sum += v
                left_counter[v] += 1
                right_counter[v] -= 1
                if right_counter[v] == 0:
                    del right_counter[v]

            left_sum += col_sum
            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            # ----- FIXED PART -----
            if left_sum > right_sum:
                cols = j + 1
                if cols == 1:
                    col = [grid[i][0] for i in range(m)]
                    if col[0] == diff or col[-1] == diff:
                        return True
                else:
                    if diff in left_counter:
                        return True
            else:
                cols = n - j - 1
                if cols == 1:
                    col = [grid[i][j+1] for i in range(m)]
                    if col[0] == diff or col[-1] == diff:
                        return True
                else:
                    if diff in right_counter:
                        return True

        return False