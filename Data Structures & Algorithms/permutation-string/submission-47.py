class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        matching = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matching += 1


        l = 0
        for r in range(len(s1), len(s2)):
            if matching == 26:
                return True

            indexRight = ord(s2[r]) - ord('a')
            count2[indexRight] += 1

            if count2[indexRight] == count1[indexRight]:
                matching += 1
            
            elif count2[indexRight] == count1[indexRight] + 1:
                matching -= 1
            

            indexLeft = ord(s2[l]) - ord('a')
            count2[indexLeft] -= 1

            if count2[indexLeft] == count1[indexLeft]:
                matching += 1
            
            elif count2[indexLeft] == count1[indexLeft] - 1:
                matching -= 1

            l += 1

        return matching == 26
            