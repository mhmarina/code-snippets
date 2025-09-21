class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0 # no volume
        # two pointers
        left = 0
        right = len(height)-1
        max_vol = -1

        while left < right:
            l_height = height[left]
            r_height = height[right]

            volume = min(l_height, r_height) * (right - left)
            if(volume > max_vol):
                max_vol = volume

            if l_height < r_height:
                left += 1
            if r_height <= l_height:
                right -= 1

        return max_vol
        