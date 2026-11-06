class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        width = max(0,min(ax2,bx2) - max(ax1,bx1))
        height = max(0,min(ay2,by2) - max(ay1,by1))

        overlapped_area = width * height

        area_r1 = (ax2-ax1) * (ay2-ay1) 
        area_r2 = (bx2-bx1) * (by2-by1)
        total_area = area_r1+area_r2

        return total_area - overlapped_area