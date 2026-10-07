class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # net = list(set(nums))
        # # net.sort()
        # for i in range(len(net)):
        #     nums[i]=net[i]
        
        # return len(net)
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1