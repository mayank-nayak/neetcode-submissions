class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []
        operatorSet = {"+", "-", "/", "*"}
        for token in tokens:
            if token not in operatorSet:
                evalStack.append(int(token))
            else:
                newOperand = 1
                operand2 = evalStack.pop()
                operand1 = evalStack.pop()
                if token == "+":
                    newOperand = operand1 + operand2
                elif token == "-":
                    newOperand = operand1 - operand2
                elif token == "*":
                    newOperand = operand1 * operand2
                elif token == "/":
                    newOperand = int(operand1 / operand2)
                evalStack.append(newOperand)

        return evalStack.pop()