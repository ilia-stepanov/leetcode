class MinStackSingleUsingOneStackWithTuples:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_value = min(self.stack[-1][1] if self.stack else float('inf'), val)
        self.stack.append((val, min_value))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        

class MinStack(MinStackSingleUsingOneStackWithTuples):
    pass



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


