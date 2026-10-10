from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        max_diff = max(diff)
        freq = [0] * (max_diff + 1)

        for d in diff:
            freq[d] += 1

        for d in range(max_diff, 0, -1):
            if k <= 0:
                break

            count = freq[d]
            if count == 0:
                continue

            moves = min(k, count)
            freq[d] -= moves
            freq[d - 1] += moves
            k -= moves

        return sum(d * d * freq[d] for d in range(max_diff + 1))
