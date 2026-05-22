from collections import defaultdict
from typing import List

# 861 翻转矩阵后的得分
# 1338
# 890
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 处理边界情况：如果矩阵为空，或只有一行，直接返回行数
        if not matrix or not matrix[0]:
            return 0
        if len(matrix) == 1:
            return 1

        pattern_count = defaultdict(int)

        for row in matrix:
            # 创建标准化模式：如果行首是1，则整行取反；如果是0，则保持不变。
            # 使用元组来存储模式，因为它可以被哈希，可以作为字典的键。
            normalized_pattern = tuple(row) if row[0] == 0 else tuple(1 - x for x in row)
            # 另一种更简洁的写法，利用异或运算实现相同的标准化效果：
            # normalized_pattern = tuple(x ^ row[0] for x in row)

            pattern_count[normalized_pattern] += 1

        # 返回出现最频繁的模式的出现次数
        return max(pattern_count.values())