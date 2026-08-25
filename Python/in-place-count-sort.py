class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count sort :D
        hm = {0: 0, 1: 0, 2: 0}
        for num in nums:
            hm[num] += 1
        
        k = 0
        for i in range(3):
            j = 0
            while j < hm[i]:
                nums[j+k] = i
                j += 1
            k += j