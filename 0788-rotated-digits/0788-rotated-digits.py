class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        valid_same = {'0', '1', '8'}
        valid_change = {'2', '5', '6', '9'}
        
        count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            valid = True
            changed = False
            
            for ch in s:
                if ch in valid_same:
                    continue
                elif ch in valid_change:
                    changed = True
                else:
                    valid = False
                    break
            
            if valid and changed:
                count += 1
        
        return count