class MinStack:

    def __init__(self):
        self.currMin = float('inf')
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.currMin = min(self.currMin, val)
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.currMin = min(self.stack)
        else:
            self.currMin = float('inf')
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        if self.currMin == float('inf'):
            return None
        else:
            return self.currMin
        
