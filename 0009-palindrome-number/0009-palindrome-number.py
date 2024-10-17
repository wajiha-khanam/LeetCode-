# 1 : Using reverse string
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
    #    str_x = str(x)
    #    if str_x == str_x[::-1]:
    #         return True
    #    else:
    #         return False

# 2 : Without using reverse string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        if x == reversed_half:
            return True
        elif x == reversed_half // 10:
            return True
        else:
            return False


