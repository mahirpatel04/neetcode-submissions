class Solution:
    def isValid(self, s: str) -> bool:
        complement = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []
        for c in s:
            if c not in complement.keys():
                stack.append(c)

            else:
                if len(stack) > 0 and stack[-1] == complement[c]:
                    stack.pop()
                
                else:
                    return False

        return len(stack) == 0 
            