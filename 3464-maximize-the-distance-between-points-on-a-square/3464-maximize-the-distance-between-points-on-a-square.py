from typing import List
import bisect

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        
        # Step 1: map to 1D
        def get_pos(x, y):
            if x == 0:
                return y
            elif y == side:
                return side + x
            elif x == side:
                return 3 * side - y
            else:
                return 4 * side - x
        
        arr = sorted(get_pos(x, y) for x, y in points)
        n = len(arr)
        per = 4 * side
        
        # duplicate for circular
        arr2 = arr + [x + per for x in arr]
        
        # Step 2: check feasibility
        def can(d):
            for i in range(n):
                count = 1
                last = arr2[i]
                
                for _ in range(k - 1):
                    # jump using binary search
                    idx = bisect.bisect_left(arr2, last + d)
                    if idx >= i + n:
                        break
                    last = arr2[idx]
                    count += 1
                
                if count == k:
                    # circular check
                    if last - arr2[i] <= per - d:
                        return True
            
            return False
        
        # Step 3: binary search
        left, right = 1, side
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans