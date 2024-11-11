class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        
    # Time - O(n)
    # Space - O(n)