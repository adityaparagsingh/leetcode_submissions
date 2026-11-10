from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # def k_works(k):
        #     #k belongs to [l,r] range
        #     hours = 0 
        #     for pile in piles:
        #         hours += ceil(pile/k) #ceil is roundup function
            
        #     return hours <= h #return True or False
        
        # l = 1
        # r = max(piles)

        # while l < r:
        #     k = l + ((r-l)//2)
        #     if k_works(k):
        #         r = k
        #     else:
        #         l = k+1
        # return l
        l, r = 1, max(piles)

        while l < r:
            mid = (l+r)//2
            hours = sum((p+mid-1)//mid for p in piles)

            if hours <= h:
                r = mid
            else:
                l = mid+1

        return l