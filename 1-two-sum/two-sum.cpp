class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();

        map<int,int> mp;

        for (int i=0;i<n;i++){
            int remaining = target - nums[i];   //9-2 = 7 we need to find 7 in the array

            if(mp.find(remaining) != mp.end()){
                return {mp[remaining],i};
            }
            mp[nums[i]]=i;
        }
        return {};
    }
};