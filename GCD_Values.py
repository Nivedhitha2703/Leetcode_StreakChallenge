from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each number
        freq = [0] * (mx + 1)
        for num in nums:
            freq[num] += 1

        # cnt[d] = count of numbers divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs with gcd exactly d
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            exact[d] = cnt[d] * (cnt[d] - 1) // 2
            multiple = 2 * d
            while multiple <= mx:
                exact[d] -= exact[multiple]
                multiple += d

        # Prefix sums of pair counts
        prefix = []
        values = []
        total = 0

        for d in range(1, mx + 1):
            if exact[d] > 0:
                total += exact[d]
                prefix.append(total)
                values.append(d)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])

        return ans
