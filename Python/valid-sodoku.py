from typing import List


class Solution:
    def isNumeric(self, s) -> bool:
        return s in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def checkSubBoxes(self, board) -> bool:
        # 9 boxes each w 3 rows, 3 cols
        for square in range(9):
            nums = []
            for i in range(3):
                for j in range(3):
                    row = (square // 3)*3 + i
                    col = (square % 3)*3 + j
                    curr = board[row][col]
                    if self.isNumeric(curr):
                        if curr in nums:
                            return False
                        nums.append(curr)
        return True

    def checkRows(self, board) -> bool:
        for i in range(9):
            nums = []
            for j in range(9):
                curr = board[i][j]
                if self.isNumeric(curr):
                    if curr in nums:
                        return False
                    nums.append(curr)
        return True
        
    def checkColumns(self, board) -> bool:
        for i in range(9):
            nums = []
            for j in range(9):
                curr = board[j][i]
                if self.isNumeric(curr):
                    if curr in nums:
                        return False
                    nums.append(curr)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkColumns(board) and self.checkRows(board) and self.checkSubBoxes(board)
    
sol = Solution()
sodoku = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
assert(sol.isValidSudoku(sodoku))

sodoku = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
assert(not sol.isValidSudoku(sodoku))
