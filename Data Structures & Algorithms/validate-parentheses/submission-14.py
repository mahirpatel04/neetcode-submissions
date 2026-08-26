class Solution:
    def isValid(self, s: str) -> bool:
        map = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c not in map.keys():
                stack.append(c)
            
            else:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0