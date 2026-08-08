class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        prev = [1]
        for i in range(rowIndex):
            row = []
            for j in range(len(prev) - 1):
                row.append(prev[j] + prev[j+1])
            prev = [1] + row + [1]
        return prev