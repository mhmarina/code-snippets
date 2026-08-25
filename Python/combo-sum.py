class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # explore all subsets of candidates. On is 2^n
        def recurse(running_sum, candidates, curr):
            if running_sum > target:
                return
            if running_sum == target:
                curr.sort()
                if curr not in res:            
                    res.append(curr)
                return
            
            for i in range(len(candidates)):
                recurse(running_sum + candidates[i], candidates, curr + [candidates[i]])
        recurse(0, candidates, [])
        return list(res)