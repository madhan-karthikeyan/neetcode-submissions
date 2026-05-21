class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            current_sum = sum(path)
            if current_sum == target:
                result.append(list(path))
                return
            if current_sum > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        backtrack(0, [])


        return result