class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            distinct = sorted(set(nums))
            ans.extend(distinct)
            for val in distinct:
                nums.remove(val)
        return ans
            
        # set1 = list(set(nums))
        # ans.append(set1)
        # newlst = [x for x in nums if x not in set1]
        # set2 = list(set(newlst))
        # ans.append(set2)
        # return ans