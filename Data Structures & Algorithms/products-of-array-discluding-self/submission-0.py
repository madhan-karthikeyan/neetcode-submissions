from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in nums:
            product *= i
        op = []
        for i in range(0, len(nums)):
            if nums[i]!=0:
                op.append(int(product/nums[i]))
                continue
            p = 1
            if Counter(nums)[0] == 1:
                for j in range(0, len(nums)):
                    if j != i:
                        p*=nums[j]
                op.append(p)
            else:
                op.append(0)
        
        return op