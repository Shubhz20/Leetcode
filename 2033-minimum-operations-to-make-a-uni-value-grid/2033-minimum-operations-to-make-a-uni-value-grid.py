from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        arr = [num for row in grid for num in row]
        
        # Step 1: check feasibility
        mod = arr[0] % x
        for num in arr:
            if num % x != mod:
                return -1
        
        # Step 2: sort
        arr.sort()
        
        # Step 3: median
        median = arr[len(arr) // 2]
        
        # Step 4: compute operations
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops