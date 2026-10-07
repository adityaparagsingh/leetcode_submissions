class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n):
            if nums[i] > 0:
                break       #i j k all positive , so sum = 0 impossible
            elif i > 0 and nums[i]==nums[i-1]:
                continue    #restart the loop if two consecutive same int appear
            j,k = i+1,n-1
            while j<k:
                sum2 =nums[i] + nums[j] + nums[k]
                if sum2 == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j,k = j+1,k-1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif sum2<0:
                    j += 1
                else:
                    k -= 1
        return ans