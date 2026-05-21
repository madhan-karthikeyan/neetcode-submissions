from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        if len(Counter(nums)) == 1:
            return 1
        nums = list(set(nums))
        hash_map = Counter(nums)
        num = min(nums)
        max_count = 0
        count = 0
        streak = True
        nums.sort()
        max_num = nums[-1]
        min_num = nums[0]
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] == nums[i]-1:
                max_num = nums[i]
                break
        for i in range(0, len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                min_num = nums[i]
                break
            print(nums[i], nums[i+1])
            
        for i in range(min_num, max_num+1):
            if i in hash_map:
                # print(i, "Yes")
                count+=1
            else:
                count = 0
                streak = False
            max_count = max(max_count, count)
            # print(i, max_count, streak)
            # print(max_count)
        return max_count