class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1   # 从右上角开始

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1      # 往左走（跳表往低值方向跳）
            else:
                row += 1      # 往下走（跳表往高值方向跳）

        return False
