class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # O(n) time complexity
        # O(n) space complexity

        # use stack to store pending opened parenthesis
        stack = []

        # Make dummy string s filled with empty chars for each char in s
        res = ["" for _ in s]
        for i, c in enumerate(s):
            # if its a closing parenthesis then check for a corresponding opening one in the stack
            if c == ")":
                # if corresponding opener found then both opener and closer are placed into result
                # otherwise the unmatched ) needs to be ignored (removed)
                if stack:
                    openIdx = stack.pop()
                    res[openIdx] = "("
                    res[i] = c

            # openers are placed into the stack where they buffer/wait for a closing parenthesis
            elif c == "(":
                stack.append(i)
            
            # all other chars are immediately placed into the resulting string
            else:
                res[i] = c        

        # returns the resulting string
        return "".join(res)