class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Group 1: indices 0 and 2
        if sorted([s1[0], s1[2]]) != sorted([s2[0], s2[2]]):
            return False
        
        # Group 2: indices 1 and 3
        if sorted([s1[1], s1[3]]) != sorted([s2[1], s2[3]]):
            return False
        
        return True