from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            # Inclusion-Exclusion over all subsets
            for mask in range(1, 1 << n):

                L = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        L = lcm(L, coins[i])

                        if L > x:
                            break

                if L > x:
                    continue

                if bits % 2 == 1:
                    total += x // L
                else:
                    total -= x // L

            return total

        # Binary search for the kth smallest amount
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
