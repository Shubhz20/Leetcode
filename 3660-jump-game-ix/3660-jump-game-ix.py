from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # stack: (max_value, start_index, end_index)
        stack = []
        
        for i, num in enumerate(nums):
            start = i
            mx = num
            
            # merge components
            while stack and num < stack[-1][0]:
                prev_max, prev_l, prev_r = stack.pop()
                start = prev_l
                mx = max(mx, prev_max)
            
            stack.append((mx, start, i))
        
        # build answer
        ans = [0] * n
        for mx, l, r in stack:
            for i in range(l, r + 1):
                ans[i] = mx
        
        return ans