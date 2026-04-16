class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in matches.values():
                stack.append(c)
            
            elif c in matches.keys():
                if len(stack) > 0:
                    if stack.pop() != matches[c]:
                        return False

                else:
                    return False
                
        if len(stack) != 0: return False
        
        return True

            