from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(x):
            return int(str(x)[::-1])
        
        seen = {}  # reverse(num) -> index
        ans = float('inf')
        
        for j, num in enumerate(nums):
            # if current number matches a previously stored reverse
            if num in seen:
                ans = min(ans, j - seen[num])
            
            # store reverse of current number
            seen[reverse_num(num)] = j
        
        return ans if ans != float('inf') else -1