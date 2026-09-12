class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        window = 0
        maxWindow = 0

        l = 0

        for r in range(len(customers)):
            # Get the length of the window we are currently looking at
            length = r - l + 1
            # If the window is longer than minutes (window too long)
            if length > minutes:
                # Subtract leftmost if we satisfied that customer due to it being the window
                # otherwise it would've been addded to the satisfied
                if grumpy[l]:
                    window -= customers[l]
                # move forward the left side of the window to get the correct length window
                l += 1
            
            # add on the new element to the correct count
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]

            # max we can save from the window is updated
            maxWindow = max(maxWindow, window)

        # we return naturally satisfied customers plus the ones where we got the most gains
        return satisfied + maxWindow

            

            


