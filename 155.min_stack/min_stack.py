class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min and self.min_stack:
            if val < self.min:
                self.min_stack.append(val)
                self.min = val
            else:
                self.min_stack.append(self.min)
        else:
            self.min = val
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.remove(self.stack[-1])
        self.min_stack.remove(self.min_stack[-1])

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
