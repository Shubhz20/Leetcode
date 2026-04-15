from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')
        
        for i in range(n):
            if words[i] == target:
                # clockwise
                right = (i - startIndex + n) % n
                # anticlockwise
                left = (startIndex - i + n) % n
                
                ans = min(ans, right, left)
        
        return ans if ans != float('inf') else -1