from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        # Step 1: check diagonal
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        # Step 2: build string
        res = [''] * n
        ch = 0
        
        for i in range(n):
            if res[i] == '':
                if ch >= 26:
                    return ""
                
                c = chr(ord('a') + ch)
                
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = c
                
                ch += 1
        
        word = ''.join(res)
        
        # Step 3: validate lcp
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i == n-1 or j == n-1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
        
        # compare with given lcp
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word