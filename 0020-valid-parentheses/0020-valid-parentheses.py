class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char in map.values():
                stack.append(char)
            elif stack and map[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
    
# Time : O(n)
# Space :  O(n)
