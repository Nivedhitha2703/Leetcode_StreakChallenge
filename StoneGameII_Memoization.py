class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def solve(i, M):
            # All piles have been taken
            if i == n:
                return 0

            # Already calculated
            if (i, M) in memo:
                return memo[(i, M)]

            remaining = suffix[i]
            best = 0

            # Try taking X piles
            for X in range(1, min(2 * M, n - i) + 1):

                newM = max(M, X)

                # Stones opponent will eventually get
                opponent = solve(i + X, newM)

                # Therefore, current player gets
                current = remaining - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return solve(0, 1)
