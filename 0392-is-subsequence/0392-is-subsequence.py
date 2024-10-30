class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == '':
            return True

        if len(s) > len(t):
            return False
        
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                if j == len(s) - 1:
                    return True
                j += 1
        return False
    
    # Time - O(len(t))
    # Space - O(1)
        