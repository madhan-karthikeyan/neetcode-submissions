class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        while low<=high:
            # mid = low + (high-low)//2
            if nums[low][0]+nums[high][0] < target:
                low = low+1
            elif nums[low][0]+nums[high][0] > target:
                high = high-1
            else:
                print("Found")
                return sorted([nums[low][1], nums[high][1]])

        return []