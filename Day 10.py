class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        left = min(nums)
        right = max(nums)

        seen = set(nums)

        ans = []

        for i in range(left, right + 1):
            if i not in seen:
                ans.append(i)

        return ans
