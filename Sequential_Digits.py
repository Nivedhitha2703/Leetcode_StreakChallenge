class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        # Try every starting digit
        for start in range(1, 10):

            num = start
            next_digit = start + 1

            # Build sequential number
            while next_digit <= 9:
                num = num * 10 + next_digit

                if low <= num <= high:
                    result.append(num)

                if num > high:
                    break

                next_digit += 1

        return sorted(result)


