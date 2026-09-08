class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        net = list(set(nums))
        net.sort()
        for i in range(len(net)):
            nums[i]=net[i]
        
        return len(net)