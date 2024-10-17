class Solution:
    def romanToInt(self, s: str) -> int:
        roman_letters = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = 0
        previous_val = 0

        for char in reversed(s):
            current_val = roman_letters[char]

            if current_val < previous_val:
                total -= current_val
            else:
                total += current_val

            previous_val = current_val
        return total