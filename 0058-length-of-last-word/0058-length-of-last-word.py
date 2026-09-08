class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # str = s.split(" ")[-1]
        # if(str == " "):
        #     strs = str[-1]
        #     return len(strs)
        
        #worst case
        # str = s.split()
        # return len(str[-1])

        #best case
        str = s.split()[::-1]
        return len(str[0])