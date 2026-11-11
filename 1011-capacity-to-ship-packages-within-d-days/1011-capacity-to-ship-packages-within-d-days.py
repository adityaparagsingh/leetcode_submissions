class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l<r:
            m = (l+r)//2
            d = 1 #tracks the number of days required.
            load = 0 #tracks the current day's total package weight.
            for w in weights:
                if load + w > m:
                    d+=1
                    load = 0   
                load += w
            if days>=d:
                r = m
            else:
                l = m+1
        return l