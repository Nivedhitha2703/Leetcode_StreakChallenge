class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        sa = list(range(n))
        rank = nums[:]
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for j in range(1, n):
                a = sa[j - 1]
                b = sa[j]

                prev = (
                    rank[a],
                    rank[a + k] if a + k < n else -1
                )

                curr = (
                    rank[b],
                    rank[b + k] if b + k < n else -1
                )

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                h = 0
                continue

            j = sa[r - 1]

            while (i + h < n and j + h < n
                   and nums[i + h] == nums[j + h]):
                h += 1

            lcp[r] = h

            if h > 0:
                h -= 1

        ans = n

        for r in range(n):
            longest = 0

            if r > 0:
                longest = max(longest, lcp[r])

            if r < n - 1:
                longest = max(longest, lcp[r + 1])

            length = longest + 1

            if length <= n - sa[r]:
                ans = min(ans, length)

        return ans
