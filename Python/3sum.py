# sliding window
# array must first be sorted
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort() is in place, sorted() returns new 
        result = []
        nums.sort()
        print(nums)  
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                curr_sum = (-nums[j])-nums[k]
                target = nums[i]
                if(curr_sum == target):
                    n = [nums[i],nums[j],nums[k]]
                    if n not in result:
                        result.append(n)
                if target < curr_sum:
                    j += 1
                else:
                    k -= 1
        return result
