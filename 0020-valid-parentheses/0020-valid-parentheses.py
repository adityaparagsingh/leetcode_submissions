class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {
            ']':'[',
            '}':'{',
            ')':'(',
        }
        for char in s:
            if char in '({[':
                stk.append(char)
            else:
                if len(stk) == 0:
                    return False #this means, the s starts with } or ] or )
                if stk[-1] != pairs[char]:
                    return False #this means, opening and closing is not in same time and correct sequence
                stk.pop()  #remove last element (if opening matches closing)
        if len(stk)==0:
            return True
        return False