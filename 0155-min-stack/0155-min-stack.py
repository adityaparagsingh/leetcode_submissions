class MinStack:

    def __init__(self):
        self.stk, self.min_stk = [],[]

    def push(self, value: int) -> None:
        self.stk.append(value)
        if not self.min_stk :
            self.min_stk.append(value)
        else:
            self.min_stk.append(min(self.min_stk[-1],value))

    def pop(self) -> None:
        if not self.stk:
            return
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()