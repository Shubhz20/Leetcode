from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        # Case 1: fix i = 0
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                ans1 = j
                break
        
        # Case 2: fix j = n-1
        for i in range(n):
            if colors[i] != colors[-1]:
                ans2 = n - 1 - i
                break
        
        return max(ans1, ans2)