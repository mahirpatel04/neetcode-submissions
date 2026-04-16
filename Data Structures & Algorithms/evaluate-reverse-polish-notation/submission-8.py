class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = set(['+', '-', '*', '/'])

        for t in tokens:
            print(stack)
            if t not in ops:
                stack.append(int(t))

            elif t == "+":
                stack.append(stack.pop() + stack.pop())

            elif t== "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(l - r)

            elif t == "*":
                stack.append(stack.pop() * stack.pop())

            elif t == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l / r))

        
        return stack[0]