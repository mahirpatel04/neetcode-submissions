class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # store open for n mins
        # given array of customers that arrive and leave at each min
        # grumpy array determines when owner is grumpy vs not

        n = len(customers)


        window_start = 0
        window_end = minutes

        maxSatisfied = 0
        maxStart = 0
        maxEnd = minutes

        while window_end <= n:
            satisfied = sum([customers[i] for i in range(window_start, window_end) if grumpy[i] == 1])

            if satisfied > maxSatisfied:
                maxSatisfied = satisfied
                maxStart = window_start
                maxEnd = window_end
                 

            window_start += 1
            window_end += 1

        print(maxSatisfied, maxStart, maxEnd)
        
        numSatisfied = 0
        for i in range(len(customers)):
            if maxStart <= i < maxEnd:
                numSatisfied += customers[i]

            elif grumpy[i] == 0:
                numSatisfied += customers[i]

        return numSatisfied            

            

