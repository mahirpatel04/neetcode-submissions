class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "/", "*"}

        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            
            elif t == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)

            elif t == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))

        return stack[-1]