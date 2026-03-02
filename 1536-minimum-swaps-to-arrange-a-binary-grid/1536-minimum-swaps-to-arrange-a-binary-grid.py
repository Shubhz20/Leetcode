class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: compute trailing zeros for each row
        trailing = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: greedy placement
        for i in range(n):
            needed = n - 1 - i
            j = i
            
            # find first row with enough trailing zeros
            while j < n and trailing[j] < needed:
                j += 1
            
            if j == n:
                return -1
            
            # bubble row j up to i
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps