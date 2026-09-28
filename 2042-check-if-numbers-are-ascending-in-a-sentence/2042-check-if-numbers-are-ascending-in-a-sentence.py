class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(" ")
        count = -1
        for i in s:
            if i.isdigit():
                if count >= int(i):
                    return False
                # elif count > int(i):
                #     return False
                else:
                    count = int(i)
        return True
        # lst = s.split(" ")
        # arr = []
        # for char in lst:
        #     if char.isdigit():
        #         arr.append(int(char))
        # for i in range(1,len(arr)):
        #     if arr[i-1]>=arr[i]:
        #         return False
        # return True