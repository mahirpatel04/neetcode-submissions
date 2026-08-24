class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        if self.stack and price >= self.stack[-1][1]:
            i = len(self.stack) - 1
            while price >= self.stack[i][1] and i >= 0:
                span += 1
                i -= 1

        self.stack.append([span, price])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)