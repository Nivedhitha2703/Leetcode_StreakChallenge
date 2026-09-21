class Solution:
    def resultArray(self, nums, k):
        result = [0] * k

        # dp[r] = number of subarrays ending at the previous
        # position whose product % k == r
        dp = [0] * k

        for num in nums:
            val = num % k

            new_dp = [0] * k

            # Start a new subarray with only nums[i]
            new_dp[val] += 1

            # Extend all previous subarrays
            for r in range(k):
                new_remainder = (r * val) % k
                new_dp[new_remainder] += dp[r]

            # Add all subarrays ending here to the answer
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result
