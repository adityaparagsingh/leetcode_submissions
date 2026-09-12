class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = []
        rightsum = []
        answer = []
        for i in range(len(nums)):
            leftsum.append(sum(nums[:i]))
            rightsum.append(sum(nums[i+1:]))
        
        for i in range(len(nums)):
            answer.append(abs(leftsum[i]-rightsum[i]))
        return answer