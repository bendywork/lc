# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。
#
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
#
# 返回一个表示每个字符串片段的长度的列表。
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。


class Solution:
    def partitionLabels(s: str) -> list[int]:
        # 1. 记录每个字母最后出现的下标
        last_pos = {char: i for i, char in enumerate(s)}

        res = []
        start = 0
        end = 0

        # 2. 贪心划分
        for i, char in enumerate(s):
            # 扩展当前片段的边界，确保包含所有当前已遇字符的最后位置
            end = max(end, last_pos[char])

            # 当扫描到当前的边界时，说明可以切分了
            if i == end:
                res.append(i - start + 1)
                start = i + 1

        return res


if __name__ == '__main__':
    s1 = "ababcbacadefegdehijhklij"
    print(Solution.partitionLabels(s1))