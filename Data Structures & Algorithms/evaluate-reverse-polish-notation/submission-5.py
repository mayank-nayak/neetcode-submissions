class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[token](a, b))
        return stack.pop()