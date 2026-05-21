from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums).most_common(k)
        lst = []
        for i in d:
            lst.append(i[0])
    
        return lst