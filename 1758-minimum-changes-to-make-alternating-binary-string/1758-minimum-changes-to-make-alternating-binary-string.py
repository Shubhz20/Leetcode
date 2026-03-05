class Solution:
    def minOperations(self, s: str) -> int:
        change0 = 0  # pattern starting with '0'
        change1 = 0  # pattern starting with '1'
        
        for i, c in enumerate(s):
            if c != ('0' if i % 2 == 0 else '1'):
                change0 += 1
            if c != ('1' if i % 2 == 0 else '0'):
                change1 += 1
        
        return min(change0, change1)