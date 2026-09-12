class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        window = 0
        maxWindow = 0

        l = 0

        for r in range(len(customers)):
            length = r - l + 1
            if length > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]

            maxWindow = max(maxWindow, window)
            print(window, satisfied, maxWindow, l, r)

        return satisfied + maxWindow

            

            


