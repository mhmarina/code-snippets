class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0

        # use set for lookups (O(1))
        num_set = set(nums)
        nums = list(num_set)
        nums.sort()

        i = 0
        while i in range(len(nums)):

            curr_len = 0
            while nums[i] + curr_len in num_set:
                curr_len += 1
            
            i = i + curr_len
            if curr_len > max_len:
                max_len = curr_len
            
        return max_len
        
            