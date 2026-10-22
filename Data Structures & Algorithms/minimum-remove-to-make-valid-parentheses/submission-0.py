class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = ["" for _ in s]
        for i, c in enumerate(s):
            if c == ")":
                if stack:
                    openIdx = stack.pop()
                    res[openIdx] = "("
                    res[i] = c

            elif c == "(":
                stack.append(i)
            
            else:
                res[i] = c        

        return "".join(res)