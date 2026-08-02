class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        n = len(piles)

        # dp[i][j] = maximum score difference the current player
        # can achieve over the opponent from piles[i...j]
        dp = [[0] * n for _ in range(n)]

        # Base case: only one pile left
        for i in range(n):
            dp[i][i] = piles[i]

        # Fill the table for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                take_left = piles[i] - dp[i + 1][j]
                take_right = piles[j] - dp[i][j - 1]

                dp[i][j] = max(take_left, take_right)

        return dp[0][n - 1] > 0
