from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list) # 键：排序后的字符串；值：原字符串列表
        for s in strs:
            key = ''.join(sorted(s)) # 排序并重新组合成字符串
            anagram_dict[key].append(s)
        return list(anagram_dict.values())

if __name__ == '__main__':
    # s = Solution()
    # print(s.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
    lst = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
    default_dict = defaultdict(list)
    print(default_dict)
    print(''.join(sorted("scx")))