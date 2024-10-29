class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.strip()
        # return len(s.split()[-1]) if s else 0
    
    # Time - O(n)
    # Space - O(n)

        i = len(s)-1
        length = 0
        while s[i] == " ":
            i -= 1
        while s[i] != " " and i >= 0:
            length += 1
            i -= 1
        return length

    # Time - O(n)
    # Space - O(1)

        