class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        res, i = 1, 0
        while res:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    res = 0
            else:
                digits.append(1)
                res = 0
            i += 1
        return digits[::-1]

    # Time - O(n)
    # Space - O(1)

     

        