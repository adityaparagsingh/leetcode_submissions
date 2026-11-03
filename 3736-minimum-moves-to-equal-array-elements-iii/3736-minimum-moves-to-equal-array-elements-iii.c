int minMoves(int* nums, int numsSize) {
    int m = nums[0], ans = 0;

    for (int i = 1; i < numsSize; i++)
        if (nums[i] > m)
            m = nums[i];

    for (int i = 0; i < numsSize; i++)
        ans += m - nums[i];

    return ans;
}