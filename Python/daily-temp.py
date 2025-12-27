class Solution:
    # stack
    def dailyTemperaturesStack(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i)) 
        
        return res

    # DP
    def dailyTemperaturesDP(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        for i in range(n-1,-1,-1):
            j = 1
            while i+j < n:
                if temperatures[i+j] > temperatures[i]:
                    res[i] = j
                    break
                else:
                    if res[i+j] == 0:
                        break
                    j += res[i+j]
        return res