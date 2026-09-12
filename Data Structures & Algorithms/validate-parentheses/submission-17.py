class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openMap = {
            "}" : "{",
            "]" : "[",
            ")" : "("
            }

        for c in s:
            if c not in openMap.keys():
                stack.append(c)
                continue
            
            if not stack or stack[-1] != openMap[c]:
                return False
            
            stack.pop()

        return len(stack) == 0