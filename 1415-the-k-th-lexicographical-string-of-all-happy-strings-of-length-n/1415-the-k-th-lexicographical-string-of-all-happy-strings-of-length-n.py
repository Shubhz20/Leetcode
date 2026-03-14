class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        
        def backtrack(s):
            if len(res) >= k:
                return
            if len(s) == n:
                res.append(s)
                return
            
            for c in "abc":
                if not s or s[-1] != c:
                    backtrack(s + c)
        
        backtrack("")
        
        if k <= len(res):
            return res[k-1]
        return ""