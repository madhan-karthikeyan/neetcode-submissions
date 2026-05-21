from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = set()
        unique = list(count.keys())
        
        for i in range(len(unique)):
            for j in range(i, len(unique)):
                x, y = unique[i], unique[j]
                z = -(x+y)
                if z not in count:
                    continue

                # Check count availability
                if x == y == z and count[x] >= 3:
                    res.add(tuple(sorted([x,y,z])))
                elif x == y and count[x] >= 2 and z != x:
                    res.add(tuple(sorted([x,y,z])))
                elif y == z and count[y] >= 2 and x != y:
                    res.add(tuple(sorted([x,y,z])))
                elif x != y and y != z and x != z:
                    res.add(tuple(sorted([x,y,z])))
        
        return [list(t) for t in res]