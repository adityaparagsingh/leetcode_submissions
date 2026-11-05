class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = list(range(1, n+1))
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1,len(arr)):
            prefix[i] = prefix[i-1] + arr[i]
        total = prefix[-1]
        for i in range(n):
            left = prefix[i]
            right = total - prefix[i] + arr[i]

            if left == right:
                return arr[i]

        return -1