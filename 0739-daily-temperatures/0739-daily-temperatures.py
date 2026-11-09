class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = [] # pair: [temp, index]
        for i,t in enumerate(temperatures):
            # i is current index and t is current temperature
            while stack and stack[-1][0]<t:
                stack_t, stack_i = stack.pop()
                ans[stack_i] = i-stack_i
            
            stack.append((t,i))
        return ans