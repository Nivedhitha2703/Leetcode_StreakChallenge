class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        digit_sum = 0

        for digit in str(n):
            if digit != '0':
                x += digit
                digit_sum += int(digit)

        if x == "":
            return 0

        return int(x) * digit_sum
