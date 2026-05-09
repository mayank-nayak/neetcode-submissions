class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openParenSet = {"(" , "{", "["}
        closeParenMap = {")":"(", "}":"{", "]":"["}
        for paren in s:
            if (paren in openParenSet):
                stack.append(paren)
            elif paren in closeParenMap:
                if not stack or stack[-1] != closeParenMap[paren]:
                    return False
                stack.pop()
            else:
                return False
        return True if not stack else False
