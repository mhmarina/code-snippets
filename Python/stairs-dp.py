class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1, 2: 2}
        return self.rec(n, memo)

    def rec(self, curr, memo):
        # base
        if curr not in memo:
            memo[curr] = self.rec(curr - 1, memo) + self.rec(curr - 2, memo)
        return memo[curr]