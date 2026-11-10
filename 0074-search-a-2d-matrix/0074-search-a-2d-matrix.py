class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m*n
        l = 0
        r = t - 1
        # 2D to 1D flattening array
        while l<=r:
            m = (l+r)//2
            i = m//n
            j = m%n
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                l = m+1
                # l-=1
            else:
                r = m-1
                # r+=1
        return False