from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val_dict = []
        res_dict= []
        for s_index, s_value in enumerate(strs):
            child_dict_val = sum([ord(s) for s in s_value])
            if  child_dict_val in val_dict:
                res_dict[val_dict.index(child_dict_val)].append(s_value)
                continue
            val_dict.append(child_dict_val)
            res_dict.append([s_value])
        return res_dict

if __name__ == '__main__':
    s = Solution()
    # res = s.groupAnagrams( strs = ["eat", "tea", "tan", "ate", "nat", "bat"])
    # print(res)
    res2 = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res2)