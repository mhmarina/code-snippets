class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left = 0
        right = n - 1

        while left < right:
            for i in range(right - left):
                up = left
                bottom = right

                temp = matrix[up][left+i]
                matrix[up][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[up+i][right]
                matrix[up+i][right] = temp

            left += 1
            right -= 1