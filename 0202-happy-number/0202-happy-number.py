class Solution:
    def isHappy(self, n: int) -> bool:
        map = set()
        while n not in map:
            map.add(n)
            n = self.sumofSquares(n)

            if n == 1:
                return True
        return False
    
    def sumofSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output


        