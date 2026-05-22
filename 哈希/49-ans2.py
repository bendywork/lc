from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val_dict = []  # 存储键： (ascii_sum, freq_signature) 元组
        res_dict = []  # 存储结果分组

        for s_value in strs:  # 如果不需要索引，可以直接遍历元素
            # 1. 计算ASCII码和（保留你的原思路）
            ascii_sum = sum(ord(s) for s in s_value)

            # 2. 【新增】生成一个字母频率签名，作为第二个条件
            # 创建一个长度为26的列表，对应a-z，记录每个字母出现的次数
            freq_count = [0] * 26
            for char in s_value:
                # 计算字母在频率表中的索引，例如 'a'->0, 'b'->1
                index = ord(char) - ord('a')
                freq_count[index] += 1
            # 将频率列表转换为一个唯一的字符串签名，例如 "1a2b0c..."
            # 使用'#'等分隔符是为了防止计数数字粘连产生歧义[3](@ref)
            freq_signature = ''.join(f"{count}#" for count in freq_count)

            # 3. 将ASCII和与频率签名组合成新键
            new_key = (ascii_sum, freq_signature)

            # 4. 后续逻辑与你原代码一致，只是判断的条件变成了元组new_key
            if new_key in val_dict:
                target_index = val_dict.index(new_key)
                res_dict[target_index].append(s_value)
            else:
                val_dict.append(new_key)
                res_dict.append([s_value])

        return res_dict