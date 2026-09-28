class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lst = s.split(" ")
        arr = []
        for char in lst:
            if char.isdigit():
                arr.append(int(char))
        for i in range(1,len(arr)):
            if arr[i-1]>=arr[i]:
                return False
        return True