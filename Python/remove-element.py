class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num == val:
                del nums[i]

        return len(nums)
        