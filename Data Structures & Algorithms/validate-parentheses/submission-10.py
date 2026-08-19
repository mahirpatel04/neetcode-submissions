class Solution:
    def isValid(self, s: str) -> bool:
        complement = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []
        for c in s:
            if c not in complement:
                stack.append(c)

            else:
                if stack and stack[-1] == complement[c]:
                    stack.pop()
                
                else:
                    return False

        return len(stack) == 0 
            