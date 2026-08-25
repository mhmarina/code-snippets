class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        indices = []
        for i, num in enumerate(nums):
            if num in unique:
                indices.append(i)
            else:
                unique.add(num)

        for i in range(len(indices)-1, -1, -1):
            del nums[indices[i]]