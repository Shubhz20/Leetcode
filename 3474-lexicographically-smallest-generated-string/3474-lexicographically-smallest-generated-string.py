class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1
        
        word = ['?'] * L
        locked = [False] * L  # 🔥 NEW
        
        # Step 1: Apply 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i+j] == '?' or word[i+j] == str2[j]:
                        word[i+j] = str2[j]
                        locked[i+j] = True   # 🔥 mark locked
                    else:
                        return ""
        
        # Step 2: Fill remaining with 'a'
        for i in range(L):
            if word[i] == '?':
                word[i] = 'a'
        
        # Step 3: Handle 'F'
        for i in range(n):
            if str1[i] == 'F':
                # check if equal
                if all(word[i+j] == str2[j] for j in range(m)):
                    
                    # need to break it
                    for j in reversed(range(m)):
                        if locked[i+j]:  # 🔥 cannot modify
                            continue
                        
                        original = word[i+j]
                        
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            if c != original:
                                word[i+j] = c
                                break
                        
                        # check if broken
                        if any(word[i+k] != str2[k] for k in range(m)):
                            break
                        else:
                            word[i+j] = original
                    else:
                        return ""
        
        return ''.join(word)