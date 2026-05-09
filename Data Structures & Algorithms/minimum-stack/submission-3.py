class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minimum = val
        else:
            self.stack.append(val - self.minimum)
            self.minimum = min(self.minimum, val)


    def pop(self) -> None:
        if not self.stack:
            return
        poppedVal = self.stack.pop()
        if poppedVal < 0:
            self.minimum = self.minimum - poppedVal


    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.minimum
        else:
            return int(self.minimum)
        

    def getMin(self) -> int:
        return int(self.minimum)
        
