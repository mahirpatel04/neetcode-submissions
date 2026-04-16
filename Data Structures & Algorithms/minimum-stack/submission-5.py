class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currMin = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.currMin = min(self.currMin, val)
        self.minStack.append(self.currMin)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.currMin = self.minStack[-1]
        else:
            self.currMin = float('inf')
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.currMin
        
