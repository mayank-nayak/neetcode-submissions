class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixMin = []
        self.minimum = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)
        self.prefixMin.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.prefixMin.pop()
        if (self.prefixMin):
            self.minimum = self.prefixMin[-1]
        else:
            self.minimum = float('inf')


    def top(self) -> int:
        return self.stack[-1] 
        

    def getMin(self) -> int:
        return self.prefixMin[-1]
        
