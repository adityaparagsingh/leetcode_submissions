class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0
        arr =[]
        for num in s:
            if num-1 not in s:
                next_num = num+1
                length = 1
                while next_num in s:
                    length +=1
                    next_num +=1
                arr.append(length)
        if len(arr)!=0:
            return max(arr)
        return 0