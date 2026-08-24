class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort list first
        nums.sort()
        results = []
        # all must add up to 0
        for i, num in enumerate(nums):
            # hold one constant
            if i > 0 and num == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while(right > left):
                total = nums[right] + nums[left] + num
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res = [num, nums[left], nums[right]]
                    results.append(res)
                    left += 1
                    right -= 1
                    # move until we get a new number
                    while(nums[left] == nums[left-1] and right > left):
                        left += 1
        
        return results