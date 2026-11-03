class Solution {
    public int minMoves(int[] nums) {
        int m = nums[0], ans = 0;

        for (int num : nums)
            m = Math.max(m, num);

        for (int num : nums)
            ans += m - num;

        return ans;
    }
}