class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans, sol = [],[] #ans is final list , sol is individual string as list 
        
        def backtrack(openn,close):
            if len(sol) == 2*n:
                ans.append(''.join(sol))
                return
            
            if openn < n:
                sol.append('(')
                backtrack(openn+1,close)
                sol.pop()
            
            if openn>close:
                sol.append(')')
                backtrack(openn,close+1)
                sol.pop()

        backtrack(0,0)
        return ans