class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0

        while left <= right:
            left_bar = heights[left]
            right_bar = heights[right]
            min_ = min(left_bar, right_bar)
            area = min_ * (right - left)
            if area > max_water:
                max_water = area
            
            if min_ == left_bar:
                left += 1
            elif min_ == right_bar:
                right -= 1
        
        return max_water