class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Store non-zero digits and their positions
        digits = []
        positions = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                positions.append(i)

        # Prefix number and prefix digit sum
        k = len(digits)
        prefix_num = [0] * (k + 1)
        prefix_sum = [0] * (k + 1)

        for i in range(k):
            prefix_num[i + 1] = (prefix_num[i] * 10 + digits[i]) % MOD
            prefix_sum[i + 1] = prefix_sum[i] + digits[i]

        ans = []

        for l, r in queries:
            # Find first non-zero digit index >= l
            left = self.lower_bound(positions, l)

            # Find first non-zero digit index > r
            right = self.lower_bound(positions, r + 1)

            if left == right:
                ans.append(0)
                continue

            # x from left to right-1
            length = right - left

            # Calculate number formed by digits[left:right]
            x = (prefix_num[right] - prefix_num[left] * pow(10, length, MOD)) % MOD

            # Calculate digit sum
            digit_sum = prefix_sum[right] - prefix_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans

    def lower_bound(self, arr, target):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
