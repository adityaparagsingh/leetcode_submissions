class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        p = [[1]]
        for i in range(1,numRows):
            prev = p[-1]
            curr = [1]
            for j in range(1,len(prev)):
                curr.append(prev[j-1]+prev[j]) #formula curr[j] = prev[j-1] + prev[j]
            curr.append(1)
            p.append(curr)
        return p