# this is the exact same solution as stairs-dp.py
class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        return self.rec(n, memo)

    def rec(self, n, memo):
        if n not in memo:
            memo[n] = self.rec(n - 1, memo) + self.rec(n - 2, memo)
        return memo[n]