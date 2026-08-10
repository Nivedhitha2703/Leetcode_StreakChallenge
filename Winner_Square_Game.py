class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            square = 1

            while square * square <= i:
                if dp[i - square * square] == False:
                    dp[i] = True
                    break

                square += 1

        return dp[n]
