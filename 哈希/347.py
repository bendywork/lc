from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        counts = Counter(nums)
        datas = counts.most_common(k)
        return [count for count,_ in datas]
