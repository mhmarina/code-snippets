class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1, 2: 2}
        return self.rec(n, memo)

    def rec(self, curr, memo):
        # base
        if curr not in memo:
            memo[curr] = self.rec(curr - 1, memo) + self.rec(curr - 2, memo)
        return memo[curr]

## recursive
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.rec(n)

    def rec(self, n):
        # base
        if(n == 0 or n == 1):
            return 1
        elif(n == 2):
            return 2
        else:
            return self.rec(n - 1) + self.rec(n - 2)