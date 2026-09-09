class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n == 2:
            return 1
        elif (n == 0):
            return 0
        else:
            return self.fib(n-1) + self.fib(n-2)