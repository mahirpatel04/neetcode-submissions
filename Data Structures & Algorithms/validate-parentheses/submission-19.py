class Solution:
    def isValid(self, s: str) -> bool:
        closeMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for c in s:
            if c not in closeMap:
                stack.append(c)
            
            else:
                if stack and stack[-1] == closeMap[c]:
                    stack.pop()

                else:
                    return False

        return len(stack) == 0
