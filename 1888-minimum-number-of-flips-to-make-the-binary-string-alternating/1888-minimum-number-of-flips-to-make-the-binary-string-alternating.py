class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s
        
        diff1 = diff2 = 0
        ans = n
        
        l = 0
        
        for r in range(len(ss)):
            expected1 = '0' if r % 2 == 0 else '1'
            expected2 = '1' if r % 2 == 0 else '0'
            
            if ss[r] != expected1:
                diff1 += 1
            if ss[r] != expected2:
                diff2 += 1
            
            if r - l + 1 > n:
                expected1 = '0' if l % 2 == 0 else '1'
                expected2 = '1' if l % 2 == 0 else '0'
                
                if ss[l] != expected1:
                    diff1 -= 1
                if ss[l] != expected2:
                    diff2 -= 1
                
                l += 1
            
            if r - l + 1 == n:
                ans = min(ans, diff1, diff2)
        
        return ans