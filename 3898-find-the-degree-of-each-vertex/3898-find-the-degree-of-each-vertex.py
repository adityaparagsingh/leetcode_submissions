class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = [0] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    ans[i]+=1
        return ans