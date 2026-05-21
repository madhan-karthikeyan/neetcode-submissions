class Solution {

    private void backtrack(int[] nums, int target, int start,
                           List<Integer> path,
                           List<List<Integer>> result) {

        // Base case → found valid combination
        if (target == 0) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i < nums.length; i++) {

            // Pruning
            if (nums[i] > target) break;

            // Choose current number
            path.add(nums[i]);

            // Reuse allowed → pass i (not i+1)
            backtrack(nums, target - nums[i], i, path, result);

            // Backtrack
            path.remove(path.size() - 1);
        }
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        Arrays.sort(nums); // helps pruning

        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, target, 0, new ArrayList<>(), result);

        return result;
    }
}
